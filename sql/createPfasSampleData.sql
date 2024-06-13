CREATE or REPLACE VIEW  podm_pfas_sample_data AS
SELECT sa.id AS id,
       sa.sample_id AS sample_id,
       sg.group_id AS group_id, 
       st.study AS study,
       st.pi as pi,
       t.units AS units,
       m.medium AS medium,
       l.city AS city,
       l.state AS state,
       l.zipcode AS zipcode,
       d.pfna_concentration AS pfna_concentration,
       d.pfna_mrl AS pfna_mrl,
       d.pfna_dl AS pfna_dl,
       d.pfna_flags AS pfna_flags,
       d.pfds_concentration AS pfds_concentration,
       d.pfds_mrl AS pfds_mrl,
       d.pfds_dl AS pfds_dl,
       d.pfds_flags AS pfds_flags,
       d.pfhxa_concentration AS pfhxa_concentration,
       d.pfhxa_mrl AS pfhxa_mrl,
       d.pfhxa_dl AS pfhxa_dl,
       d.pfhxa_flags AS pfhxa_flags,
       d.pfoa_concentration AS pfoa_concentration,
       d.pfoa_mrl AS pfoa_mrl,
       d.pfoa_dl AS pfoa_dl,
       d.pfoa_flags AS pfoa_flags,
       d.pfos_concentration AS pfos_concentration,
       d.pfos_mrl AS pfos_mrl,
       d.pfos_dl AS pfos_dl,
       d.pfos_flags AS pfos_flags,
       d.pfba_concentration AS pfba_concentration,
       d.pfba_mrl AS pfba_mrl,
       d.pfba_dl AS pfba_dl,
       d.pfba_flags AS pfba_flags,
       d.pfdoa_concentration AS pfdoa_concentration,
       d.pfdoa_mrl AS pfdoa_mrl,
       d.pfdoa_dl AS pfdoa_dl,
       d.pfdoa_flags AS pfdoa_flags,
       d.pfpea_concentration AS pfpea_concentration,
       d.pfpea_mrl AS pfpea_mrl,
       d.pfpea_dl AS pfpea_dl,
       d.pfpea_flags AS pfpea_flags,
       d.pfhps_concentration AS pfhps_concentration,
       d.pfhps_mrl AS pfhps_mrl,
       d.pfhps_dl AS pfhps_dl,
       d.pfhps_flags AS pfhps_flags,
       d.pfunda_concentration AS pfunda_concentration,
       d.pfunda_mrl AS pfunda_mrl,
       d.pfunda_dl AS pfunda_dl,
       d.pfunda_flags AS pfunda_flags,
       d.pfbs_concentration AS pfbs_concentration,
       d.pfbs_mrl AS pfbs_mrl,
       d.pfbs_dl AS pfbs_dl,
       d.pfbs_flags AS pfbs_flags,
       d.pfpes_concentration AS pfpes_concentration,
       d.pfpes_mrl AS pfpes_mrl,
       d.pfpes_dl AS pfpes_dl,
       d.pfpes_flags AS pfpes_flags,
       d.pfns_concentration AS pfns_concentration,
       d.pfns_mrl AS pfns_mrl,
       d.pfns_dl AS pfns_dl,
       d.pfns_flags AS pfns_flags,
       d.pfhpa_concentration AS pfhpa_concentration,
       d.pfhpa_mrl AS pfhpa_mrl,
       d.pfhpa_dl AS pfhpa_dl,
       d.pfhpa_flags AS pfhpa_flags,
       d.pfhxs_concentration AS pfhxs_concentration,
       d.pfhxs_mrl AS pfhxs_mrl,
       d.pfhxs_dl AS pfhxs_dl,
       d.pfhxs_flags AS pfhxs_flags,
       d.pfda_concentration AS pfda_concentration,
       d.pfda_mrl AS pfda_mrl,
       d.pfda_dl AS pfda_dl,
       d.pfda_flags AS pfda_flags
FROM podm_sample sa
INNER JOIN podm_study st ON st.study_id=sa.study_id
INNER JOIN podm_technique t ON t.technique_id=sa.technique_id
INNER JOIN podm_medium m ON m.medium_id=sa.medium_id
INNER JOIN podm_location l ON l.location_id=sa.location_id
INNER JOIN podm_sample_groups sg ON sg.group_id=sa.group_id
INNER JOIN podm_pfas_data d ON d.sample_id=sa.sample_id;
