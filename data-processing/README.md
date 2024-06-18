The Python scripts in this directory where used in processing the intermediate data files archived 
on Microsoft Teams. The processing involved changes the enabled the data to be ingeted into the
PFAS Observation Data Model.

processNonTargeted.py - This script converted the non targeted data to the column form:
	sample_id,short_name,long_name,flags,measurement

createGeom.py - This script used existing longitude and latitude values to create Well
	Know Binary (WKB) values for use the Django REST Framework (DRF) GIS.

createGroupID.py - This script took at input AHHS_Sample_Locations_WithZip.csv and NCS_Serum_Dust_crosswalk_share.csv
	converting them to a common form: water_sample_id dust_sample_id serum_sample_id   
	and then combining them into a single file for ingest into the podm_sample_groups table

createLocationIngest.py - This script takes as input the PFAS_Sample_Locations_Dust.csv and
	PFAS_Sample_Locations_Water.csv converting the data to SQL for ingest

changeCsvColumnNames.py - This script converts the intermediate data files columns to lowercase

PFASNamingClassificationInfoColumns2Lowercase.py - This script converts the PFAS Naming Classification file columns
	to lowercase 
