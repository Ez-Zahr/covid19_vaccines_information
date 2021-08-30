"""covid19_vaccines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('initdb/', views.initDB, name='initDB'),
    
    path('country/', views.CountryIndexView.as_view(), name='country_index'),
    path('sponsor/', views.SponsorIndexView.as_view(), name='sponsor_index'),
    path('vaccine/', views.VaccineIndexView.as_view(), name='vaccine_index'),
    path('sponsormanufacturesvaccine/', views.SponsorManufacturesVaccineIndexView.as_view(), name='sponsormanufacturesvaccine_index'),
    path('vaccinetrialsincountry/', views.VaccineTrialsInCountryIndexView.as_view(), name='vaccinetrialsincountry_index'),
    
    path('country/create/', views.createCountry, name='createCountry'),
    path('sponsor/create/', views.createSponsor, name='createSponsor'),
    path('vaccine/create/', views.createVaccine, name='createVaccine'),
    path('sponsormanufacturesvaccine/create/', views.createSponsorManufacturesVaccine, name='createSponsormanufacturesvaccine'),
    path('vaccinetrialsincountry/create/', views.createVaccineTrialsInCountry, name='createVaccinetrialsincountry'),
    
    path('country/<str:pk>/', views.CountryDetailView.as_view(), name='detail'),
    
    path('country/edit/<str:pk>/', views.editCountry, name='editCountry'),
    path('sponsor/edit/<int:pk>/', views.editSponsor, name='editSponsor'),
    path('vaccine/edit/<int:pk>/', views.editVaccine, name='editVaccine'),
    path('sponsormanufacturesvaccine/edit/<int:pk>/', views.editSponsorManufacturesVaccine, name='editSponsormanufacturesvaccine'),
    path('vaccinetrialsincountry/edit/<int:pk>/', views.editVaccineTrialsInCountry, name='editVaccinetrialsincountry'),
    
    path('country/delete/<str:pk>/', views.deleteCountry, name='deleteCountry'),
    path('sponsor/delete/<int:pk>/', views.deleteSponsor, name='deleteSponsor'),
    path('vaccine/delete/<int:pk>/', views.deleteVaccine, name='deleteVaccine'),
    path('sponsormanufacturesvaccine/delete/<int:pk>/', views.deleteSponsorManufacturesVaccine, name='deleteSponsormanufacturesvaccine'),
    path('vaccinetrialsincountry/delete/<int:pk>/', views.deleteVaccineTrialsInCountry, name='deleteVaccinetrialsincountry'),

    path('sponsorsincountry/<str:countryCode>/', views.SponsorsInCountry.as_view(), name='sponsors_in_country'),
    path('sponsorsincountry/', views.SponsorsInCountry.as_view(), name='sponsors_in_country'),

    path('vaccinesbysponsor/<str:sponsor>/', views.VaccinesBySponsor.as_view(), name='vaccines_by_sponsor'),
    path('vaccinesbysponsor/', views.VaccinesBySponsor.as_view(), name='vaccines_by_sponsor'),

    path('vaccinesincountry/<str:countryCode>/', views.VaccinesInCountry.as_view(), name='vaccines_in_country'),
    path('vaccinesincountry/', views.VaccinesInCountry.as_view(), name='vaccines_in_country'),
    
    path('sponsorsvaccinesstatus/<str:vaccineStatus>/', views.SponsorsVaccinesStatus.as_view(), name='sponsors_vaccines_status'),
    path('sponsorsvaccinesstatus/', views.SponsorsVaccinesStatus.as_view(), name='sponsors_vaccines_status'),

    path('trialsincountries/', views.TrialsInCountries.as_view(), name="trials_in_countries"),

    path('sponsorscountries/', views.SponsorsCountries.as_view(), name='sponsors_countries'),
]
