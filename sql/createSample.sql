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

CREATE INDEX IF NOT EXISTS sample_sample_id_index
ON podm_sample(sample_id);

CREATE INDEX IF NOT EXISTS sample_group_id_index
ON podm_sample(group_id);

CREATE INDEX IF NOT EXISTS sample_study_id_index
ON podm_sample(study_id);

CREATE INDEX IF NOT EXISTS sample_medium_id_index
ON podm_sample(medium_id);

CREATE INDEX IF NOT EXISTS sample_location_id_index
ON podm_sample(location_id);

CREATE INDEX IF NOT EXISTS sample_technique_id_index
ON podm_sample(technique_id);
