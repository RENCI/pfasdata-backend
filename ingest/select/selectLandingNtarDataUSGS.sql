\copy (SELECT id AS sample_id,pfprs AS "PFPrS", genx_num AS "GENX", fosa AS "FOSA", f6_2fts AS "F6_2FTS" FROM podm_pfas_in_tapwater_usgs) TO '/projects/pfas/data/nonTargetedUSGS.csv' DELIMITER ',' CSV HEADER;
