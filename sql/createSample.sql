CREATE TABLE IF NOT EXISTS podm_sample (
    sample_id SERIAL PRIMARY KEY,
    study_id INT REFERENCES podm_study(study_id),
    medium_id INT REFERENCES podm_medium(medium_id),
    location_id INT REFERENCES podm_location(location_id),
    technique_id INT REFERENCES podm_technique(technique_id),
    sample VARCHAR(30)
);
