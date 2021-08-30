## Table of Contents
1. [Database](#database)
2. [Author(s)](#author)
3. [Database Description](#description)
4. [Installing the Django Server](#installing-the-django-server)
5. [Running the Django Server](#running-the-django-server)
6. [Updating the Requirements](#updating-the-requirements)
 
# Database
covid19_vaccines_information

# Author(s)
Enoc Carranza,
Wael Mobeirek,
Aziz Alzahrani.

# Database Description
We are tracking information about COVID-19 vaccines across the globe that are being developed, going under clinical trials, or approved. Each vaccine will include the candidate name, mechanism of vaccination, list of sponsors, background details, and a list of countries participating in the trials. For each sponsor, we’re storing the name of the sponsor, as well as the country that the sponsor is based in. Moreover, we’re storing the name and the country code for all the countries in the world. 

# Installing the Django Server
1. Make sure that you have Python 3.9.5 by running the following in the command line: `python --version`
2. Clone/download the repository to your local machine
3. Using the command line, go to the main directory: `cd YOURPATH\cs480---course-project-covid19_vaccines_information\covid19_vaccines_app`
4. Create a python virual environment: `python -m venv env`
5. Activate the virtual environment: `./env\Scripts\activate`
6. Install the required depedencies: `pip install -r requirements.txt`
7. Make sure that the MySQL database is setup according to initializeDB.sql
8. Go to the covid_vaccines app directory `covid19_vaccines_app\covid19_vaccines\covid19_vaccines\` and copy the `.env.example` then paste it and rename it to `.env`
9. Using a text editor, open `covid19_vaccines_app\covid19_vaccines\covid19_vaccines\.env` and update `MYSQL_USER` and `MYSQL_PASSWORD` to match your local MySQL server.
10. Change the directory to the Django project directory: `cd cs480---course-project-covid19_vaccines_information\covid19_vaccines_app\covid19_vaccines`
11. Run the Django server: `python manage.py runserver`

Note: these instructions are on windows 10 machines. It should be similar on other systems as well.

# Running the Django Server
1. Activate the virtual environment: `./env\Scripts\activate`
2. Change the directory to the Django project directory: `cd covid19_vaccines_app\covid19_vaccines`
3. Run the Django server: `python manage.py runserver`

# Updating the Requirements
1. Using the command line, go to the main directory: `cd YOURPATH\cs480---course-project-covid19_vaccines_information\covid19_vaccines_app`
2. Install the required depedencies: `pip install -r requirements.txt`
3. Run the Django server