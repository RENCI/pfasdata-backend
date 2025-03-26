INSERT INTO podm_location (latitude, longitude, site_id, site_type, detects, sum)
SELECT DISTINCT latitude, longitude, station_na, site_type, detects, sum_pfas
FROM podm_pfas_in_tapwater_usgs
ORDER BY station_na;
