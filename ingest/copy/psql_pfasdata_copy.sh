PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f data_copy_landing.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f data_copy_model_pfas.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f data_copy_model_ntar.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f data_copy_model_sample_groups.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f data_copy_landing_location.sql
PGPASSWORD=xxxxxxxx psql -U pfasdata -d pfasdata_prod -p 5432 -h localhost -f data_copy_name_class_info.sql
