CREATE MATERIALIZED VIEW podm_pfas_sample_data2 AS
SELECT sa.id AS id,
       sa.sample_id AS sample_id,
       st.study AS study,
       sa.date AS date,
       st.year AS year,
       st.pi as pi,
       t.units AS units,
       m.medium AS medium,
       l.site_id AS site_id,
       l.site_type AS site_type,
       l.latitude AS latitude,
       l.longitude AS longitude, 
       l.detects AS sample_detects,
       l.sum AS sample_sum,
       d.pfmpa_concentration AS pfmpa_concentration, 
       d.pfmpa_mrl AS pfmpa_mrl,
       d.pfmba_concentration AS pfmba_concentration,
       d.pfmba_mrl AS pfmba_mrl,
       d.pfta_concentration AS pfta_concentration,
       d.pfta_mrl AS pfta_mrl ,
       d.netfosaa_concentration AS netfosaa_concentration,
       d.netfosaa_mrl AS netfosaa_mrl,
       d.x82fts_concentration AS x82fts_concentration,
       d.x82fts_mrl AS x82fts_mrl,
       d.hfpoda_concentration AS hfpoda_concentration,
       d.hfpoda_mrl AS hfpoda_mrl,
       d.x62fts_concentration AS x62fts_concentration,
       d.x62fts_mrl AS x62fts_mrl,
       d.nfdha_concentration AS nfdha_concentration,
       d.nfdha_mrl AS nfdha_mrl,
       d.pfuna_concentration AS pfuna_concentration,
       d.pfuna_mrl AS pfuna_mrl,
       d.pfeesa_concentration AS pfeesa_concentration,
       d.pfeesa_mrl AS pfeesa_mrl,
       d.nmefosaa_concentration AS nmefosaa_concentration,
       d.nmefosaa_mrl AS nmefosaa_mrl,
       d.x9clpf3ons_concentration AS x9clpf3ons_concentration,
       d.x9clpf3ons_mrl AS x9clpf3ons_mrl,
       d.x11clpf3ouds_concentration AS x11clpf3ouds_concentration,
       d.x11clpf3ouds_mrl AS x11clpf3ouds_mrl,
       d.adona_concentration AS adona_concentration,
       d.adona_mrl AS adona_mrl,
       d.x42fts_concentration AS x42fts_concentration,
       d.x42fts_mrl AS x42fts_mrl,
       d.pftrda_concentration AS pftrda_concentration,
       d.pftrda_mrl AS pftrda_mrl,
       d.genx_concentration AS genx_concentration, 
       d.fosa_concentration AS fosa_concentration, 
       d.f6_2fts_concentration AS f6_2fts_concentration, 
       d.pfprs_concentration AS pfprs_concentration
FROM podm_sample sa
INNER JOIN podm_study st ON st.study_id=sa.study_id
INNER JOIN podm_technique t ON t.technique_id=sa.technique_id
INNER JOIN podm_medium m ON m.medium_id=sa.medium_id
INNER JOIN podm_location l ON l.location_id=sa.location_id
INNER JOIN podm_sample_groups sg ON sg.group_id=sa.group_id
INNER JOIN podm_pfas_data2 d ON d.sample_id=sa.sample_id;
