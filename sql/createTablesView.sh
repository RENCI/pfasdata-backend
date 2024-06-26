# The tables in the PFAS Observationn Data Model are not managed by Django, so they are not
# created with "python manage.py migrate" is run. They need to be created by running the SQL 
# files in the sql directory (pfasdata-backend/sql) of the Repo. This file should be modified
# changing the PGPASSWORD to the one you use for your DB and then run.
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createNtarData.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createPfasData.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createLocation.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createMedium.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createStudy.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createTechnique.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createSampleGroup.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createSample.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createPfasSampleData.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createNtarSampleData.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createLandingAHHSDustData.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createLandingAHHSWaterData.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createLandingLocation.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createLandingNCSDustData.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_dev -p 5432 -h localhost -f createLandingNCSSerumData.sql
