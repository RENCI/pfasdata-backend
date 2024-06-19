# pfasdata-backend 
This repository contains the software for creating a Django Rest Framework application that serves PFAS data from postgresql/postgis database.

# Installation 

## Build docker images and containers for the backend   

After downloading or cloning the repository, change your directory to the project root directory:  

### Build for dev

Create .env.dev and .env.dev.db files  

In the project root directory create a file named .env.dev and add the following information to it:  

DEBUG=1  
SECRET_KEY=change_me  
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]  
SQL_ENGINE=django.contrib.gis.db.backends.postgis  
SQL_DATABASE=pfasdata_dev  
SQL_USER=pfasdata  
SQL_PASSWORD=xxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres 

Add your own password. 

Then create a file named .env.dev.db and add the following information to it:  

POSTGRES_USER=pfasdata  
POSTGRES_PASSWORD=xxxxxxxxx  
POSTGRES_DB=pfasdata_dev

Add your own password here as well.  

### Run docker-compose

Before running docker-compose edit the docker-compose.yml file changing the line where 
the volume for the project data is created:

- /PATH/TO/DATA/DIRECTORY:/projects/pfas/data

This should be changed to the directory on you machine where that data is located.

Then from the project root directory run docker-compose on the development docker-compose.yml file:  

docker-compose up -d --build   

### Run migrate to create tables in DB

docker-compose exec web python manage.py migrate --no-input

### Run createsuperuser to create admin:

docker-compose exec web python manage.py createsuperuser

Below are the prompts with responses when running createsuperuser:

username: admin  
email: your@email.address  
password: xxxxxxx

Replace email and password with appropriate values.

Login to: http://localhost:8000/admin/ and create user pfas, including password. The user pfas will be used 
too access data from the API using a JSON web token (JWT). 

### Build for prod 

Create .env.prod and .env.prod.db files

In the project root directory create a file named .env.prod and add the following information to it:

DEBUG=1
SECRET_KEY=change_me  
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]  
SQL_ENGINE=django.contrib.gis.db.backends.postgis  
SQL_DATABASE=pfasdata_prod  
SQL_USER=pfasdata  
SQL_PASSWORD=xxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres  

Add your own password.

Add the domain name of the machine your using to DJANGO_ALLOWED_HOSTS. For example:

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 pfas-db-dev.mdc.renci.unc.edu [::1]

Then create a file named .env.prod.db and add the following information to it:

POSTGRES_USER=pfasdata  
POSTGRES_PASSWORD=xxxxxxxxx  
POSTGRES_DB=pfasdata_prod

Add your own password here as well.

### Run docker-compose

In the next step, from the project root directory run docker-compose on the development docker-compose.prod.yml file:

docker-compose -f docker-compose.prod.yml up -d --build

### Run migrate to create tables in DB

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

### Run createsuperuser to create admin:

docker-compose exec web python manage.py createsuperuser

Below are the prompts with responses when running createsuperuser:

username: admin  
email: your@email.address  
password: xxxxxxx

Replace email and password with appropriate values.

Login to: https://pfas-db-dev.mdc.renci.unc.edu/admin/ and create user pfas, including password. The user pfas will be used 
too access data from the API using a json web token (JWT).

### Create non managed DB tables

The tables in the PFAS Observation Data Model are not managed by Django, so they are not created with "python manage.py migrate" is run. They need to be created by running the SQL files in the SQL directory (pfasdata-backend/sql) of the Repo. The createTablesView.sh file should be modified changing the PGPASSWORD to the one you use for your DB and then run to create these tables:

./createTablesView.sh

After the tables have been created move all the PFAS data files to the directory that you declared in the docker-compose.yml, and ingest this data into the DB in the appropriate tables. After this data has been ingested run ingestPfasSamples.py by using the shell script ingestCommands.sh:

./ingestCommands.sh 

To run ingestPfasSamples.py the following Python module need to be installed:

pandas  
psycopg  
argparse  
dotenv

# Create backup of DB using cronjob:

The directory /pfasdata-backend/dbbackup, in this repo, contains files used to setup and run backups with a cronjob. These files are:

 - pd_backup_rotated.sh the script that creates rotating backups. This script is currently setup to for five day (removes sixth day) rotating backups. 
 - pg_backup.config the script that configures how pd_backup_rotated.sh is run, including setting the days for the rotating backup  
 - cronjob.sh an example cronjob file for running a cronjob of pd_backup_rotated.sh at 12 AM.
