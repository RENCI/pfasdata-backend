CREATE TABLE IF NOT EXISTS podm_sample_groups (
    group_id SERIAL PRIMARY KEY,
    water_sample_id VARCHAR(30),
    dust_sample_id VARCHAR(30),
    serum_sample_id VARCHAR(30)
);
