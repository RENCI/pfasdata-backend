## Data Ingest Scripts
This directory contains scripts for ingesting data into the PFAS Observation Database. There are two 
sub-directories copy and insert. 

The copy directory contains scripts that use the SQL COPY command to copy CSV data files into the
landing, non-targeted, targeted, sample groups and PFAS naming classification table.

The insert directory contains scripts that use the SQL INSERT data into the peripheral (location, 
medium, sample group, study and technique) meta tables.

 * README.md - This README.md
 * ingestPfasSamples.py - ingest samples and related IDs from PODM peripheral tables into the podm_sample table
 * ingestCommands.sh - examples of how to run ingestPfasSamples.py
 * copy:
   * data_copy_landing.sql - copy commands for ingest into the landing data tables
   * data_copy_landing_location.sql - copy command for ingest into the landing location table
   * data_copy_model_ntar.sql - copy command for ingest into the non-targeted table
   * data_copy_model_pfas.sql - copy commands for ingest into the targeted table
   * data_copy_model_sample_groups.sql - copy command for ingest into the sample groups table
   * data_copy_name_class_info.sql - copy command for ingest into the PFAS naming classification table
   * psql_pfasdata_copy.sh - psql commands to run the above copy commands (need to add password)
 * insert:
   * insertLocation.sql - insert command for ingest data into the location table
   * insertMedium.sql - insert command for ingest data into the medium table
   * insertSampleGroup.sql - insert command for ingest data into the sample group table
   * insertStudy.sql - insert command for ingest data into the study table
   * insertTechnique.sql - insert command for ingest data into the technique table
   * insertPfasMetaData.sh - psql commands to run the above insert commands (need to add password)
