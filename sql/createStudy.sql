CREATE TABLE IF NOT EXISTS podm_study (
    study_id SERIAL PRIMARY KEY,
    study VARCHAR(100),
    pi VARCHAR(50),
    year NUMERIC(4,0),
    detects INT,
    sum NUMERIC
);
