INSERT INTO podm_pfas_data (sample_id,pfna_concentration,pfds_concentration,pfhxa_concentration,pfoa_concentration,pfos_concentration,pfba_concentration,pfpea_concentration,pfhps_concentration,pfbs_concentration,pfpes_concentration,pfhpa_concentration,pfhxs_concentration,pfda_concentration)
SELECT id AS sample_id,pf AS pfna_concentration, pfds_num AS pfds_concentration,
       pfhxa AS pfhxa_concentration, pfoa AS pfoa_concentration, pfos AS pfos_concentration,
       pfba AS pfba_concentration, pfpea AS pfpea_concentration, pfhps AS pfhps_concentration,
       pfbs AS pfbs_concentration, pfpes AS pfpes_concentration, pfhpa AS pfhpa_concentration,
       pfhxs AS pfhxs_concentration, pfda_num AS pfda_concentration
FROM podm_pfas_in_tapwater_usgs;
