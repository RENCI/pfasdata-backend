INSERT INTO podm_pfas_data2 (sample_id, genx_concentration, fosa_concentration, f6_2fts_concentration, pfprs_concentration)
SELECT id AS sample_id, genx_num AS genx_concentration, fosa AS fosa_concentration, f6_2fts AS f6_2fts_concentration, pfprs AS pfprs_concentration
FROM podm_pfas_in_tapwater_usgs;
