COPY zcta_2020_centroids(zcta, lat, lon) 
FROM '/projects/pfas/data/ZCTA_2020_Centroids.csv'
DELIMITER ','
CSV HEADER;
