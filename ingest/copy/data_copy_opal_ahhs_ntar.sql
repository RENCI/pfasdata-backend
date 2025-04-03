COPY podm_ntar_data(sample_id,pfas_short_name,pfas_long_name,flags,measurement)
FROM '/projects/pfas/data/AHHSNontargetedDatasetWater_Model.csv'
DELIMITER ','
CSV HEADER;
