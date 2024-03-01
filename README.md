# pfasdata-backend 
This repository contains the software for creating a Django Rest Framework application that serves PFAS data from postgresql/postgis database.

# Installation 

## Build docker images and containers for the backend   

After downloading or cloning the repository, change your directory to the project root directory:  

### Build for dev

Create .env.dev and .env.dev.db files  

In the project root directory create a file named .env and add the following information to it:  

DEBUG=1  
SECRET_KEY=change_me  
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]  
SQL_ENGINE=timescale.db.backends.postgis  
SQL_DATABASE=pfasdata_dev
SQL_USER=pfasdata 
SQL_PASSWORD=xxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres  

Add your own password.  

Then create a file nameed .env.db and add the following information to it:  

POSTGRES_USER=pfasdata  
POSTGRES_PASSWORD=xxxxxxxxx  
POSTGRES_DB=pfasdata_dev

Add your own password here as well.  

### Run docker-compose

In the next step, from the project root directory run docker-compose on the development docker-compose.yml file:  

docker-compose up -d --build   

### Run migrate to create tables in DB

docker-compose exec web python manage.py migrate --no-input

### Build for prod 

Create .env.prod and .env.prod.db files

In the project root directory create a file named .env and add the following information to it:

DEBUG=1
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]
SQL_ENGINE=timescale.db.backends.postgis
SQL_DATABASE=pfasdata_prod
SQL_USER=pfasdata
SQL_PASSWORD=xxxxxxxxx
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres

Add your own password.

Then create a file nameed .env.db and add the following information to it:

POSTGRES_USER=pfasdata     
POSTGRES_PASSWORD=xxxxxxxxx    
POSTGRES_DB=pfasdata_prod

Add your own password here as well.

### Run docker-compose

In the next step, from the project root directory run docker-compose on the development docker-compose.prod.yml file:

docker-compose -f docker-compose.prod.yml up -d --build

### Run migrate to create tables in DB

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
