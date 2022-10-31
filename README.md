

This project is designed by WVSSM team 
@developer : https://github.com/mohamadch91

# Inventory and Gap Analysis System
# Dependencies
for install dependencies please read Project installation file



# Installation
1. Clone the project
2. install the requirments use 
    `pip install -r requirements.txt`
3. defult database is sqlite
    for change the data base to postgress you must create postgres database
## Postgress installation

1. login as postgress user use: 
    `sudo su — postgres`
2. then use data base mode:
    `psql`
3. Create data base:
    `create database nw_db;`
4. Set password for postgres user:
    `\password postgres;`
5. exit the postgres console:
    `\q`
## Edit python files
1. open inventory/settings.py
2. comment following lines:
    ` DATABASES = {`
     `'default': {`
         `'ENGINE': 'django.db.backends.sqlite3',`
         `'NAME': str(BASE_DIR / 'db.sqlite3'),`
     `}`
     `}`
3. uncomment following lines like this:
       ` DATABASES = {`
    `     'default': {`
    ` 'ENGINE': 'django.db.backends.postgresql',`
     `   'NAME': 'nw_db',`
       ` 'USER': 'postgres',`
    `    'PASSWORD': 'changed_password',`
       ` 'HOST': 'localhost',`
      `  'PORT': '',`
`}`
`}`
##  Load initial datas
 for loading data base tables and please use this commands:
    `python3 manage.py makemigrations`
    `python3 manage.py migrate`
then you must load initial data
    `python3 mannage.py loaddata initial.json`
now you have user admin with password admin
## Run project
for run the project 
    `python3 manage.py runserver 0.0.0.0:8000`
you can check localhost:8000 or your server ip for successfully setup 
