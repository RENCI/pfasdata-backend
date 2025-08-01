CREATE TABLE IF NOT EXISTS zcta_2020_centroids (
    location_id SERIAL PRIMARY KEY,
    zcta VARCHAR(7),
    lat NUMERIC,
    lon NUMERIC
);
