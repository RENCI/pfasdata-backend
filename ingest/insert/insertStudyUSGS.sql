INSERT INTO podm_study (study, year, pi)
SELECT DISTINCT study, sampleyear, 'USGS'
FROM podm_pfas_in_tapwater_usgs
ORDER BY study, sampleyear;
