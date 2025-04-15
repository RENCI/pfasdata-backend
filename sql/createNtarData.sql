CREATE TABLE IF NOT EXISTS podm_ntar_data (
    data_id SERIAL PRIMARY KEY,
    sample_id VARCHAR(100),
    pfas_short_name VARCHAR(25),
    pfas_long_name VARCHAR(120),
    mrl NUMERIC
    flags VARCHAR(15),
    measurement NUMERIC
);

CREATE INDEX IF NOT EXISTS ntar_data_sample_id_index
ON podm_ntar_data(sample_id);
