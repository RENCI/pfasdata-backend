COPY podm_sample_groups(water_sample_id,dust_sample_id,serum_sample_id)
FROM '/projects/pfas/data/sampleGroups.csv'
DELIMITER ','
CSV HEADER;
