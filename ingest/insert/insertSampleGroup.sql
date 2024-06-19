INSERT INTO  podm_sample_groups(water_sample_id, dust_sample_id, serum_sample_id)
VALUES
('None','None','None');

UPDATE podm_sample_groups
SET group_id = -9
WHERE water_sample_id = 'None' and dust_sample_id = 'None' and serum_sample_id = 'None';
