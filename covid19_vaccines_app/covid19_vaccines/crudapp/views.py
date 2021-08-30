from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from .models import Country, TbUser, Vaccine, Sponsor, Vaccinetrialsincountry, Sponsormanufacturesvaccine
from .forms import CountryForm, RegisterForm, SponsorForm, SponsormanufacturesvaccineForm, VaccineForm, VaccinetrialsincountryForm, SponsorsInCountry
from django.views.generic import ListView, DetailView
import os.path

# Create your views here.

# Classes

class CountryIndexView(ListView):
    template_name = 'country/index.html'
    context_object_name = 'country_list'

    def get_queryset(self):
        return Country.objects.raw('SELECT * FROM country;')

class VaccineIndexView(ListView):
    template_name = 'vaccine/index.html'
    context_object_name = 'vaccine_list'

    def get_queryset(self):
        return Vaccine.objects.raw('SELECT * FROM vaccine;')

class SponsorIndexView(ListView):
    template_name = 'sponsor/index.html'
    context_object_name = 'sponsor_list'

    def get_queryset(self):
        return Sponsor.objects.raw('SELECT * FROM sponsor;')

class VaccineTrialsInCountryIndexView(ListView):
    template_name = 'vaccinetrialsincountry/index.html'
    context_object_name = 'vaccinetrialsincountry_list'

    def get_queryset(self):
        return Vaccinetrialsincountry.objects.raw('SELECT * FROM vaccinetrialsincountry;')

class SponsorManufacturesVaccineIndexView(ListView):
    template_name = 'sponsormanufacturesvaccine/index.html'
    context_object_name = 'sponsormanufacturesvaccine_list'

    def get_queryset(self):
        return Sponsormanufacturesvaccine.objects.raw('SELECT * FROM sponsormanufacturesvaccine;')

class CountryDetailView(DetailView):
    model = Country
    template_name = 'country-detail.html'

class VaccinesInCountry(ListView):
    model = Vaccine
    template_name = 'non_trivial/vaccines_in_country.html'
    context_object_name = 'vaccine_list'

    def get_queryset(self):
        if ("countryCode" in self.kwargs):
            return Vaccine.objects.raw("SELECT vaccine.VaccineID, VaccineName, VaccineMechanism, VaccineStatus, VaccineDetails "
             + "FROM vaccine "
             + "INNER JOIN sponsormanufacturesvaccine ON vaccine.VaccineID = sponsormanufacturesvaccine.VaccineID " 
             + "INNER JOIN sponsor ON sponsormanufacturesvaccine.SponsorID = sponsor.SponsorID "
             + "WHERE SponsorCountry = '" + self.kwargs["countryCode"] + "';")
        else:
            return None

class SponsorsInCountry(ListView):
    model = Sponsor
    template_name = 'non_trivial/sponsors_in_country.html'
    context_object_name = 'sponsorsincountry_list'

    def get_queryset(self):
        if ("countryCode" in self.kwargs):
            return Sponsor.objects.raw("SELECT * FROM sponsor WHERE SponsorCountry = '" + self.kwargs["countryCode"] + "'")
        else:
            return None

class SponsorsCountries(ListView):
    model = Sponsor
    template_name = 'non_trivial/sponsors_countries.html'
    context_object_name = 'sponsorscountries_list'

    def get_queryset(self):
        cursor = connection.cursor()
        cursor.execute("SELECT SponsorName, CountryName FROM sponsor JOIN country ON sponsor.SponsorCountry = country.CountryCode;")
        result = cursor.fetchall()
        cursor.close()
        return result

class VaccinesBySponsor(ListView):
    model = Vaccine
    template_name = 'non_trivial/vaccines_by_sponsor.html'
    context_object_name = 'vaccine_list'

    def get_queryset(self):
        if ("sponsor" in self.kwargs):
            return Vaccine.objects.raw("SELECT vaccine.VaccineID, VaccineName, VaccineMechanism, VaccineStatus, VaccineDetails "
             + "FROM vaccine "
             + "INNER JOIN sponsormanufacturesvaccine ON vaccine.VaccineID = sponsormanufacturesvaccine.VaccineID " 
             + "INNER JOIN sponsor ON sponsormanufacturesvaccine.SponsorID = sponsor.SponsorID "
             + "WHERE SponsorName = '" + self.kwargs["sponsor"] + "';")
        else:
            return None

class SponsorsVaccinesStatus(ListView):
    model = Sponsor
    template_name = 'non_trivial/sponsors_vaccines_status.html'
    context_object_name = 'sponsorsvaccinesstatus_list'

    def get_queryset(self):
        if ("vaccineStatus" in self.kwargs):
            cursor = connection.cursor()
            cursor.execute("SELECT SponsorName, VaccineName, VaccineStatus FROM sponsor " +
                                        "JOIN sponsormanufacturesvaccine USING(SponsorID) " +
                                        "JOIN vaccine USING(VaccineID) " +
                                        "WHERE VaccineStatus = '" + self.kwargs["vaccineStatus"] + "'")
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            return None

class TrialsInCountries(ListView):
    model = Country
    template_name = 'non_trivial/trials_in_countries.html'
    context_object_name = 'trialsincountries_list'

    def get_queryset(self):
        return Country.objects.raw("SELECT CountryCode, CountryName AS name, " +
        "(SELECT count(*) FROM vaccinetrialsincountry WHERE Country.CountryCode = vaccinetrialsincountry.CountryCode " +
        "GROUP BY CountryCode) AS trials FROM Country")

# Functions

def createCountry(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO country (CountryCode, CountryName, CountryVaccinated)" +
             "VALUES('" + form.cleaned_data['countrycode'] + "', '" + form.cleaned_data['countryname'] + "', " + str(form.cleaned_data['countryvaccinated']) + ");")
            cursor.close()
            
            return redirect('country_index')
    form = CountryForm()
    return render(request,'create.html',{'form': form})

def editCountry(request, pk, template_name='edit.html'):
    country = get_object_or_404(Country, pk=pk)
    form = CountryForm(request.POST or None, instance=country)
    if form.is_valid():
        cursor = connection.cursor()
        cursor.execute("UPDATE country " +
        "SET CountryCode = '" + form.cleaned_data['countrycode'] + "', CountryName = '" + form.cleaned_data['countryname'] + "', CountryVaccinated = " + str(form.cleaned_data['countryvaccinated']) + " WHERE CountryCode = '" + str(pk) + "';")
        cursor.close()

        return redirect('country_index')
    return render(request, template_name, {'form':form})

def deleteCountry(request, pk, template_name='confirm_delete.html'):
    country = get_object_or_404(Country, pk=pk)
    if request.method=='POST':
        cursor = connection.cursor()       
        sql = "DELETE FROM country WHERE CountryCode='" + pk + "';"
        cursor.execute(sql)
        cursor.close()
        return redirect('country_index')
    return render(request, template_name, {'object':country})

def createVaccine(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO vaccine (VaccineName, VaccineMechanism, VaccineStatus, VaccineDetails)" +
             "VALUES('" + form.cleaned_data['vaccinename'] + "', '" + form.cleaned_data['vaccinemechanism'] + "', '" + form.cleaned_data['vaccinestatus'] + "', '" + form.cleaned_data['vaccinedetails'] + "');")
            cursor.close()
            
            return redirect('vaccine_index')
    form = VaccineForm()
    return render(request,'create.html',{'form': form})

def editVaccine(request, pk, template_name='edit.html'):
    vaccine = get_object_or_404(Vaccine, pk=pk)
    form = VaccineForm(request.POST or None, instance=vaccine)
    if form.is_valid():
        cursor = connection.cursor()
        cursor.execute("UPDATE vaccine " +
        "SET VaccineName = '" + form.cleaned_data['vaccinename'] + "', VaccineMechanism = '" + form.cleaned_data['vaccinemechanism'] + "', VaccineStatus = '" + form.cleaned_data['vaccinestatus'] + "', VaccineDetails = '" + form.cleaned_data['vaccinedetails'] + "'" + " WHERE VaccineID = '" + str(pk) + "';")
        cursor.close()
        return redirect('vaccine_index')
    return render(request, template_name, {'form':form})

def deleteVaccine(request, pk, template_name='confirm_delete.html'):
    vaccine = get_object_or_404(Vaccine, pk=pk)
    if request.method=='POST':
        cursor = connection.cursor()       
        sql = "DELETE FROM vaccine WHERE VaccineID=" + str(pk) + ";"
        cursor.execute(sql)
        cursor.close()
        return redirect('vaccine_index')
    return render(request, template_name, {'object':vaccine})

def createSponsor(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST)
        if form.is_valid():

            cursor = connection.cursor()
            cursor.execute("INSERT INTO sponsor (SponsorName, SponsorCountry)" +
             "VALUES('" + form.cleaned_data['sponsorname'] + "', '" + form.cleaned_data['sponsorcountry'].countrycode + "');")
            cursor.close()

            return redirect('sponsor_index')
    form = SponsorForm()
    return render(request,'create.html',{'form': form})

def editSponsor(request, pk, template_name='edit.html'):
    sponsor = get_object_or_404(Sponsor, pk=pk)
    form = SponsorForm(request.POST or None, instance=sponsor)
    if form.is_valid():
        cursor = connection.cursor()
        cursor.execute("UPDATE sponsor " +
        "SET SponsorName = '" + form.cleaned_data['sponsorname'] + "', SponsorCountry = '" + form.cleaned_data['sponsorcountry'].countrycode + "'" + " WHERE SponsorID = '" + str(pk) + "';")
        cursor.close()
        return redirect('sponsor_index')
    return render(request, template_name, {'form':form})

def deleteSponsor(request, pk, template_name='confirm_delete.html'):
    sponsor = get_object_or_404(Sponsor, pk=pk)
    if request.method=='POST':
        cursor = connection.cursor()       
        sql = "DELETE FROM sponsor WHERE SponsorID=" + str(pk) + ";"
        cursor.execute(sql)
        cursor.close()
        return redirect('sponsor_index')
    return render(request, template_name, {'object':sponsor})

def createVaccineTrialsInCountry(request):
    if request.method == 'POST':
        form = VaccinetrialsincountryForm(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            print(form)
            sql = "INSERT INTO vaccinetrialsincountry (VaccineID, CountryCode) VALUES(" + str(form.cleaned_data['vaccineid'].vaccineid) + ", '" + str(form.cleaned_data['countrycode'].countrycode) + "');"
            print(sql)
            cursor.execute(sql)
            cursor.close()
            return redirect('vaccinetrialsincountry_index')
    form = VaccinetrialsincountryForm()
    return render(request,'create.html',{'form': form})

def editVaccineTrialsInCountry(request, pk, template_name='edit.html'):
    vaccinetrialsincountry = get_object_or_404(Vaccinetrialsincountry, pk=pk)
    form = VaccinetrialsincountryForm(request.POST or None, instance=vaccinetrialsincountry)
    print(pk)
    if form.is_valid():
        cursor = connection.cursor()
        cursor.execute("UPDATE vaccinetrialsincountry " +
        "SET VaccineID = " + str(form.cleaned_data['vaccineid'].vaccineid) + ", CountryCode = '" + form.cleaned_data['countrycode'].countrycode + "'" + " WHERE TrialID = '" + str(pk) + "';")
        cursor.close()

        return redirect('vaccinetrialsincountry_index')
    return render(request, template_name, {'form':form})

def deleteVaccineTrialsInCountry(request, pk, template_name='confirm_delete.html'):
    vaccinetrialsincountry = get_object_or_404(Vaccinetrialsincountry, pk=pk)
    if request.method=='POST':
        cursor = connection.cursor()       
        sql = "DELETE FROM vaccinetrialsincountry WHERE TrialID=" + str(pk) + ";"
        cursor.execute(sql)
        cursor.close()
        return redirect('vaccinetrialsincountry_index')
    return render(request, template_name, {'object':vaccinetrialsincountry})

def createSponsorManufacturesVaccine(request):
    if request.method == 'POST':
        form = SponsormanufacturesvaccineForm(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO sponsormanufacturesvaccine (SponsorID, VaccineID)" +
             "VALUES(" + str(form.cleaned_data['sponsorid'].sponsorid) + ", '" + str(form.cleaned_data['vaccineid'].vaccineid) + "');")
            cursor.close()
            return redirect('sponsormanufacturesvaccine_index')
    form = SponsormanufacturesvaccineForm()
    return render(request,'create.html',{'form': form})

def editSponsorManufacturesVaccine(request, pk, template_name='edit.html'):
    sponsormanufacturesvaccine = get_object_or_404(Sponsormanufacturesvaccine, pk=pk)
    form = SponsormanufacturesvaccineForm(request.POST or None, instance=sponsormanufacturesvaccine)
    if form.is_valid():
        cursor = connection.cursor()
        cursor.execute("UPDATE sponsormanufacturesvaccine " +
        "SET SponsorID = " + str(form.cleaned_data['sponsorid'].sponsorid) + ", VaccineID = " + str(form.cleaned_data['vaccineid'].vaccineid) + " " + " WHERE ManufacturingID = '" + str(pk) + "';")
        cursor.close()
        return redirect('sponsormanufacturesvaccine_index')
    return render(request, template_name, {'form':form})

def deleteSponsorManufacturesVaccine(request, pk, template_name='confirm_delete.html'):
    sponsormanufacturesvaccine = get_object_or_404(Sponsormanufacturesvaccine, pk=pk)
    if request.method=='POST':
        cursor = connection.cursor()       
        sql = "DELETE FROM sponsormanufacturesvaccine WHERE ManufacturingID=" + str(pk) + ";"
        cursor.execute(sql)
        cursor.close()
        return redirect('sponsormanufacturesvaccine_index')
    return render(request, template_name, {'object':sponsormanufacturesvaccine})

def landing(request):
    return render(request, "landing/index.html", {})

def home(request):
    return render(request, "home/index.html", {})

def login(request):
    user = request.POST.get("username")
    password = request.POST.get("password")
    if (user and password):
        queryset = TbUser.objects.raw("SELECT * FROM tb_user WHERE username = '" + user + "' AND password = '" + password + "'")
        if (len(queryset) > 0):
            return redirect('home')
        return render(request, "auth/login.html", {'msg': 'Invalid Username or Password'})
    return render(request, "auth/login.html", {})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RegisterForm()
    return render(request, "auth/register.html", {'form': form})

def initDB(request):
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, "initDB.txt")
    print(path)
    file = open(path, "r")
    cursor = connection.cursor()
    cursor.execute(file.read())
    cursor.close()
    return redirect('home')