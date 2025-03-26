INSERT INTO podm_location (latitude, longitude, site_id, site_type)
SELECT DISTINCT lat, lon, pwsid, 'PWSID' AS site_type
FROM landing_usmr5_data 
ORDER BY pwsid;
