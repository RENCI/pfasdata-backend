PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f PFAS_Sample_Locations_Serum.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f PFAS_Sample_Locations_Dust.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f PFAS_Sample_Locations_Water.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertMedium.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertStudy.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertTechnique.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f insertSampleGroup.sql
