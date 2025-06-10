# opal-backend 
This repository is part of OPAL (Observational PFAS Access paneL), and it contains the software for creating a Django Rest Framework application that serves PFAS data from postgresql/postgis database.

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
SQL_DATABASE=xxxxxxxx_dev  
SQL_USER=xxxxxxxx  
SQL_PASSWORD=xxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres 

Add your own database name, user and password. 

Then create a file named .env.dev.db and add the following information to it:  

POSTGRES_USER=xxxxxxx  
POSTGRES_PASSWORD=xxxxxxxxx  
POSTGRES_DB=xxxxxxxx_dev

Add your own database name, user and password here as well.  

### Run docker-compose

Before running docker-compose edit the docker-compose.yml file changing the line where 
the volume for the project data is created:

- /PATH/TO/DATA/DIRECTORY:/xxxxxxxx/pfas/data

This should be changed to the directory on you machine where that data is located.

Then from the project root directory run docker-compose on the development docker-compose.yml file:  

docker-compose up -d --build   

### Run migrate to create tables in DB

docker-compose exec web python manage.py migrate --no-input

### Run createsuperuser to create admin:

docker-compose exec web python manage.py createsuperuser

Below are the prompts with responses when running createsuperuser:

username: xxxxx  
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
SQL_DATABASE=xxxxxxxx_prod  
SQL_USER=xxxxxxxx  
SQL_PASSWORD=xxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres  

Add your own database name, user and  password.

Add the domain name of the machine your using to DJANGO_ALLOWED_HOSTS. For example:

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 pfas-db-dev.xxx.xxx.unc.edu [::1]

Then create a file named .env.prod.db and add the following information to it:

POSTGRES_USER=xxxxxxxx  
POSTGRES_PASSWORD=xxxxxxxxx  
POSTGRES_DB=xxxxxxxx_prod

Add your own database name, user and password here as well.

### Run docker-compose

In the next step, from the project root directory run docker-compose on the development docker-compose.prod.yml file:

docker-compose -f docker-compose.prod.yml up -d --build

### Run migrate to create tables in DB

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

### Run createsuperuser to create admin:

docker-compose exec web python manage.py createsuperuser

Below are the prompts with responses when running createsuperuser:

username: xxxxx  
email: your@email.address  
password: xxxxxxx

Replace email and password with appropriate values.

Login to: https://pfas-db-dev.mdc.renci.unc.edu/admin/ and create user pfas, including password. The user pfas will be used 
too access data from the API using a JSON web token (JWT).

### Create non managed DB tables

The tables in the PFAS Observation Data Model (PODM) are not managed by Django, so they are not created with "python manage.py migrate" 
is run. They need to be created by running the SQL files in the SQL directory (opal-backend/sql) of the Repo. The 
createTablesView.sh file should be modified changing the PGPASSWORD to the one you use for your DB and then run to create these 
tables:

 * ./createTablesView.sh

After the tables have been created run the following shell command:

 * ./insertPfasMetaData.sh - you need to be in the opal-backend/ingest/insert when you run this command

The shell script insertPfasMetaData.sh will ingest the meta data for the peripheral tables (location, medium, sample group, 
study and technique) in PODM.

After that data has been ingested move all the PFAS CSV data files to the directory that you declared in the docker-compose.yml. 
Then run the following shell command:

 * ./psql_pfasdata_copy.sh - you need to be in the opal-backend/ingest/copy when you run this command

This will ingest all of the CSV data files into the landing, non-targeted, targeted, sample groups and PFAS naming 
classification table.
 
After that data has been ingested run ingestPfasSamples.py by using the shell script ingestCommands.sh:

 * ./ingestCommands.sh 

This will ingest data into the podm_sample data which is the central table in PODM. 
To run ingestPfasSamples.py the following Python module need to be installed:

 - pandas  
 - psycopg  
 - argparse  
 - dotenv

# Create backup of DB using cronjob:

The directory /opal-backend/dbbackup, in this repo, contains files used to setup and run backups with a cronjob. 
These files are:

 - pd_backup_rotated.sh the script that creates rotating backups. This script is currently setup to for five day (removes sixth day) rotating backups. 
 - pg_backup.config the script that configures how pd_backup_rotated.sh is run, including setting the days for the rotating backup  
 - cronjob.sh an example cronjob file for running a cronjob of pd_backup_rotated.sh at 12 AM.
