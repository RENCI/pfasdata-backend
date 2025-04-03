COPY podm_ntar_data(sample_id,pfas_short_name,mrl,measurement)
FROM '/projects/pfas/data/UCMR5NonTargeted_OPAL.csv'
DELIMITER ','
CSV HEADER;
