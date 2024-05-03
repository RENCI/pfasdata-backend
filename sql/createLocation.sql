CREATE TABLE IF NOT EXISTS podm_location (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(200),
    state VARCHAR(2),
    zipcode VARCHAR(7),
    latitude NUMERIC,
    longitude NUMERIC
);
