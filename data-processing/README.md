## Data Processing Scripts
The Python scripts in this directory where used in processing the intermediate data files archived on
Microsoft Teams OneDrive. The processing involves changes that enabled the data to be ingested into the
PFAS Observation Data Model.

 * processAHHS_NonTargeted.py - This script converts the non targeted data to the column form:
   - sample_id,short_name,long_name,flags,measurement.
   - Below is an example of how to run this script:
     * python processAHHS_NonTargeted.py --inPath /PATH/TO/bin_data/Bin_processed_data/ingest/ --outPath /PATH/TO/dataIngest/csv_files/ --inFile AHHSNontargetedDatasetWater_Column.csv --outFile AHHSNontargetedDatasetWater_OPAL.csv
     * python processUSGS_NonTargeted.py --inPath /PATH/TO/bin_data/Bin_processed_data/ingest/ --outPath /PATH/TO/dataIngest/csv_files/ --inFile nontargetedUSGS.csv --outFile USGSNontargeted_OPAL.csv
     * python processUCMR5_NonTargeted.py --inPath /PATH/TO/bin_data/Bin_processed_data/ingest/ --outPath /PATH/TO/dataIngest/csv_files/ --inFile nontargetedUCMR5.csv --outFile UCMR5Nontargeted_OPAL.csv
     * where --inPath is the path to the original data, --outPath is the path to the file output by this script, and --inFile is the name of the ogiginal data file.
 * createGeom.py - This script uses existing longitude and latitude values to create Well Know Binary (WKB) values for use the Django REST Framework (DRF) GIS.
   - Below is an example of how to run this script:
     * python createGeom.py --inputPath /PATH/TO/ORIGINAL/DATAFILE --outputPath /PATH/TO/PROCESSED/DATAFILE/ --inputFileName ORIGINALDATAFILE.csv --outputFileName PROCESSEDATAFILE.csv --lonName long_final --latName lat_final
 * createGroupID.py - This script takes as input AHHS_Sample_Locations_WithZip.csv and NCS_Serum_Dust_crosswalk_share.csv converting them to a common form:
   - water_sample_id dust_sample_id serum_sample_id and then combining them into a single file for ingest into the podm_sample_groups table.
   - Below is an example of how to run this script:
     * python createGroupID.py --inLocPath /PATH/TO/LOCATIONZIPCODE/DATAFILE.csv --inCrossPath /PATH/TO/CROSSWALK/DATAFILE/ --outputPath /PATH/TO/PROCESSED/DATAFILE/ --inLocFile LOCATIONZIPCODEFILE.csv --inCrossFile CROSWALKFILE.csv
 * createLocationIngest.py - This script takes as input the PFAS_Sample_Locations_Dust.csv and PFAS_Sample_Locations_Water.csv converting the data to SQL for ingest.
   - Below is an example of how to run this script:
     * python createLocationIngest.py --inPath --sqlPath --dustFile --waterFile 
 * changeCsvColumnNames.py - This script converts the intermediate data files columns to lowercase.
 * PFASNamingClassificationInfoColumns2Lowercase.py - This script converts the PFAS Naming Classification file 
columns to lowercase.
