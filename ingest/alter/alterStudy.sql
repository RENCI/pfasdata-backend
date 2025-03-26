ALTER TABLE podm_study
DROP COLUMN station,
DROP COLUMN site_type,
DROP COLUMN detects,
DROP COLUMN sum;

ALTER TABLE podm_study ADD detects INT;
ALTER TABLE podm_study ADD sum NUMERIC;
