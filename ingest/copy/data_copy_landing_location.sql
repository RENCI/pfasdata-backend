COPY landing_location(water_sample_id,dust_sample_id,city,state,zipcode)
FROM '/projects/pfas/data/AHHS_Sample_Locations_WithZip.csv'
DELIMITER ','
CSV HEADER;
