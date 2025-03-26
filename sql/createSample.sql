CREATE TABLE IF NOT EXISTS podm_sample (
    id SERIAL PRIMARY KEY,
    sample_id VARCHAR(100),
    date DATE NULL,
    group_id INT REFERENCES podm_sample_groups(group_id),
    study_id INT REFERENCES podm_study(study_id),
    medium_id INT REFERENCES podm_medium(medium_id),
    location_id INT REFERENCES podm_location(location_id),
    technique_id INT REFERENCES podm_technique(technique_id)
);
