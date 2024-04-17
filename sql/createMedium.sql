CREATE TABLE IF NOT EXISTS podm_medium (
    medium_id SERIAL PRIMARY KEY,
    medium VARCHAR(20),
    description VARCHAR(300),
    comments VARCHAR(500),
    creation_date DATE,
    modified_date DATE
);
