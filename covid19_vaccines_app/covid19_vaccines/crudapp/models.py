# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# To update from a legacy database:  python manage.py inspectdb > models.py
from django.db import models


class Country(models.Model):
    countrycode = models.CharField(db_column='CountryCode', primary_key=True, max_length=3)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', unique=True, max_length=50)  # Field name made lowercase.
    countryvaccinated = models.PositiveBigIntegerField(db_column='CountryVaccinated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Sponsor(models.Model):
    sponsorid = models.AutoField(db_column='SponsorID', primary_key=True)  # Field name made lowercase.
    sponsorname = models.CharField(db_column='SponsorName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    sponsorcountry = models.ForeignKey(Country, models.DO_NOTHING, db_column='SponsorCountry', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sponsor'


class Sponsormanufacturesvaccine(models.Model):
    manufacturingid = models.AutoField(db_column='ManufacturingID', primary_key=True)  # Field name made lowercase.
    sponsorid = models.ForeignKey(Sponsor, models.CASCADE, db_column='SponsorID', blank=True, null=True)  # Field name made lowercase.
    vaccineid = models.ForeignKey('Vaccine', models.CASCADE, db_column='VaccineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sponsormanufacturesvaccine'
        unique_together = (('sponsorid', 'vaccineid'),)


class TbUser(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tb_user'


class Vaccine(models.Model):
    vaccineid = models.AutoField(db_column='VaccineID', primary_key=True)  # Field name made lowercase.
    vaccinename = models.CharField(db_column='VaccineName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vaccinemechanism = models.CharField(db_column='VaccineMechanism', max_length=80, blank=True, null=True)  # Field name made lowercase.
    vaccinestatus = models.CharField(db_column='VaccineStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vaccinedetails = models.TextField(db_column='VaccineDetails', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vaccine'


class Vaccinetrialsincountry(models.Model):
    trialid = models.AutoField(db_column='TrialID', primary_key=True)  # Field name made lowercase.
    vaccineid = models.ForeignKey(Vaccine, models.CASCADE, db_column='VaccineID', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.ForeignKey(Country, models.CASCADE, db_column='CountryCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vaccinetrialsincountry'
        unique_together = (('vaccineid', 'countrycode'),)
