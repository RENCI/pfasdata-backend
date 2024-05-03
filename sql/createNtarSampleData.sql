CREATE or REPLACE VIEW  podm_ntar_sample_data AS
SELECT sa.sample_id AS sample_id,
       sa.sample AS sample,
       st.study AS study,
       st.pi as pi,
       t.units AS units,
       m.medium AS medium,
       l.city AS city,
       l.state AS state,
       l.zipcode AS zipcode,
       d.pfas_short_name AS pfas_short_name,
       d.pfas_long_name AS pfas_long_name,
       d.flags AS flags,
       d.measurement AS measurement
FROM podm_sample sa
INNER JOIN podm_study st ON st.study_id=sa.study_id
INNER JOIN podm_technique t ON t.technique_id=sa.technique_id
INNER JOIN podm_medium m ON m.medium_id=sa.medium_id
INNER JOIN podm_location l ON l.location_id=sa.location_id
INNER JOIN podm_ntar_data d ON d.sample=sa.sample;
