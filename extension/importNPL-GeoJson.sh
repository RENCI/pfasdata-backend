# Use ogr2ogr to ingest NPL sites into DB
ogr2ogr -f "PostgreSQL" PG:"dbname=xxxxx user=xxxxx password=xxxxxx host=localhost port=xxxxx" /projects/pfas/data/Superfund_National_Priorities_List_NPL_Sites_with_Status_Information_Albers.geojson -nln superfund_albers_national_priorities_list

# Update geometry to Albers Equal Area, EPSG:102008
SELECT UpdateGeometrySRID('public', 'superfund_albers_national_priorities_list', 'wkb_geometry', 102008);
