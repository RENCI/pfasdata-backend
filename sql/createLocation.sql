CREATE TABLE IF NOT EXISTS podm_location (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(200),
    state VARCHAR(2),
    zipcode VARCHAR(7),
    site_id VARCHAR(80),
    site_type VARCHAR(20,
    detects INT,
    sum NUMERIC, 
    latitude NUMERIC,
    longitude NUMERIC
);
