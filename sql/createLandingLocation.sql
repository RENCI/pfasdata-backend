CREATE TABLE IF NOT EXISTS landing_location (
    location_id SERIAL PRIMARY KEY,
    water_sample_id VARCHAR(30),
    dust_sample_id VARCHAR(30),
    city VARCHAR(200),
    state VARCHAR(2),
    zipcode VARCHAR(7)
);
