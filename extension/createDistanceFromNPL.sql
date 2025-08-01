CREATE TABLE IF NOT EXISTS pfas_sites_distance_from_npl (
    pfas_sample_id VARCHAR(100) PRIMARY KEY,
    study VARCHAR(100),
    miles INT,
    pi VARCHAR(50),
    units VARCHAR(20),
    medium VARCHAR(20),
    pfas_longitude NUMERIC,
    pfas_latitude NUMERIC,
    ogc_fid INT,
    npl_site_name VARCHAR(300),
    npl_latitude NUMERIC,
    npl_longitude NUMERIC
);
