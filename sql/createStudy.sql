CREATE TABLE IF NOT EXISTS podm_study (
    study_id SERIAL PRIMARY KEY,
    study VARCHAR(100),
    station VARCHAR(200),
    site_type VARCHAR(50),
    year NUMERIC(4,0),
    detects NUMERIC,
    sum NUMERIC,
    pi VARCHAR(50)
);
