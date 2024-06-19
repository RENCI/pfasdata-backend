PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertLocation.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertMedium.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertStudy.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertTechnique.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertSampleGroup.sql
