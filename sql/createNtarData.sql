CREATE TABLE IF NOT EXISTS podm_ntar_data (
    data_id SERIAL PRIMARY KEY,
    sample VARCHAR(30),
    pfas_short_name VARCHAR(25),
    pfas_long_name VARCHAR(120),
    flags VARCHAR(15),
    measurement NUMERIC
);
