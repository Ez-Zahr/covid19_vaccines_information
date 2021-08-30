from django import forms
from django.db.models import fields
from .models import Country, Sponsor, TbUser, Vaccine, Vaccinetrialsincountry, Sponsormanufacturesvaccine

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = "__all__"

class VaccinetrialsincountryForm(forms.ModelForm):
    class Meta:
        model = Vaccinetrialsincountry
        fields = "__all__"

class SponsormanufacturesvaccineForm(forms.ModelForm):
    class Meta:
        model = Sponsormanufacturesvaccine
        fields = "__all__"

class SponsorsInCountry(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"

class SponsorsCountries(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"

class SponsorsVaccinesStatus(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"
        exclude =  ('manufacturingid',)

class TrialsInCountries(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"
        exclude = ('trialid',)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = TbUser
        fields = "__all__"