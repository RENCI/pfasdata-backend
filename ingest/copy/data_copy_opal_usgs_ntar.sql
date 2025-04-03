COPY podm_ntar_data(sample_id,pfas_short_name,measurement)
FROM '/projects/pfas/data/USGSNonTargeted_OPAL.csv'
DELIMITER ','
CSV HEADER;
