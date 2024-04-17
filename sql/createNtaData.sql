CREATE TABLE IF NOT EXISTS podm_nta_data (
    data_id SERIAL PRIMARY KEY,
    sample VARCHAR(30),
    pfas_name VARCHAR(100),
    measurement NUMERIC
);
