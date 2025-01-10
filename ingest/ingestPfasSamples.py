#!/usr/bin/env python
# coding: utf-8

# import modules
import os
import pandas as pd
import psycopg
from psycopg import sql
import argparse
from dotenv import find_dotenv
from dotenv import load_dotenv

# Import and load enviroment files
env_file = find_dotenv(".env.dev")
load_dotenv(env_file)
env_file = find_dotenv(".env.db.dev")
load_dotenv(env_file)

def insertSample(landingTable,studyId,techniqueId,mediumId):
    ''' This function inserts IDs into the podm_sample table. Three of the IDs are inputs to this
        function (e.g. studyId,techniqueId,mediumId), two are set to single values and later updated
        (e.g. group_id, location_id), and one (i.e. study_id) is obtained from one of four landing 
        tables.
        Parameters
            landingTable: string
                One of four landing tables (e.g. landing_ahhs_dust_data, landing_ahhs_water_data
                landing_ncsdust_data, landing_ncsserum_data)                
            studyId: string
                A studyId
            techniqueId: string
                A techniqueId
            mediumId: string
                A mediumId 
        Returns
            Inserts IDs into the  podm_sample table
    '''
    try:
        # Create connection to database, set autocommit, and get cursor
        with psycopg.connect(dbname=os.environ['SQL_DATABASE'],
                             user=os.environ['SQL_USER'],
                             host=os.environ['SQL_HOST'],
                             port=os.environ['SQL_PORT'],
                             password=os.environ['SQL_PASSWORD'],
                             autocommit=True) as conn:
            cur = conn.cursor()
            
            # Run query
            cur.execute(sql.SQL("""INSERT INTO podm_sample(sample_id, study_id, group_id, medium_id, 
                                                           location_id, technique_id)
                                       SELECT sample_id, %s, %s, %s, %s, %s
                                       FROM {}""").format(sql.Identifier(landingTable)),
                                       [studyId, -9, mediumId, 1, techniqueId,])              
                
            # Close cursor and database connection
            cur.close()
            conn.close()
            
    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)

def addGroupId(sgidcname,mediumId):
    ''' This function updates the podm_sample table where group_id values from the
        podm_sample_groups table for a specific mediumId and where the podm_sample
        sample_id equals the sample_id from one of three sample ID columns in the 
        podm_sample_groups table. 
        Parameters
            sgidcname: string
                The sample group column name (e.g. water_sample_id, dust_sample_id, serum_sample_id)
            mediumId: string
                A mediumId
        Returns
            Updates the podm_sample table with group_id values 
    '''
    try:
        # Create connection to database, set autocommit, and get cursor
        with psycopg.connect(dbname=os.environ['SQL_DATABASE'],
                             user=os.environ['SQL_USER'],
                             host=os.environ['SQL_HOST'],
                             port=os.environ['SQL_PORT'],
                             password=os.environ['SQL_PASSWORD'],
                             autocommit=True) as conn:
            cur = conn.cursor()
            
            # Run query
            cur.execute(sql.SQL("""UPDATE podm_sample ps
                                   SET group_id = sg.group_id
                                   FROM podm_sample_groups sg
                                   WHERE sg.{sgidcname}=ps.sample_id AND 
                                   ps.medium_id = %s 
                                   """).format(sgidcname=sql.Identifier(sgidcname)),
                                   [mediumId])                

                
            # Close cursor and database connection
            cur.close()
            conn.close()
            
    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def addLocationId(sgidcname,mediumId):
    ''' This function updates the podm_sample table with location_id from the podm_location
        table, for a specific mediumId. This update includes a join between the podm_location
        table and landing_location table on zipcode. This enables a where equal statement 
        between the podm_sample table sample_id and one of three (water_sample_id, dust_sample_id,
        serum_sample_id) landing_location sample_ids.
        Parameters
            sgidcname: string
                The sample group column name (e.g. water_sample_id, dust_sample_id, serum_sample_id)
            mediumId: string
                A mediumId 
        Returns
            Updates the podm_sample table with location_id values
    '''
    try:
        # Create connection to database, set autocommit, and get cursor
        with psycopg.connect(dbname=os.environ['SQL_DATABASE'],
                             user=os.environ['SQL_USER'],
                             host=os.environ['SQL_HOST'],
                             port=os.environ['SQL_PORT'],
                             password=os.environ['SQL_PASSWORD'],
                             autocommit=True) as conn:
            cur = conn.cursor()
            
            # Run query
            cur.execute(sql.SQL("""UPDATE podm_sample ps
                                   SET location_id = pl.location_id
                                   FROM podm_location pl
                                   INNER JOIN landing_location ll ON ll.zipcode=pl.zipcode
                                   WHERE ll.{sgidcname}=ps.sample_id AND ps.medium_id = %s 
                                   """).format(sgidcname=sql.Identifier(sgidcname)),
                                   [mediumId])                

                
            # Close cursor and database connection
            cur.close()
            conn.close()
            
    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def getStudyId(study,pi):
    ''' This function queries the podm_study table for a study_id
        related to a study and pi
        Parameters
            study: string
                A study (e.g. AHHS, ncsSerum, ncsDust)
            pi: string
                A PI (e.g. HUD, EPA)
        Returns
            A study_id value
    '''
    try:
        # Create connection to database, set autocommit, and get cursor
        with psycopg.connect(dbname=os.environ['SQL_DATABASE'],
                             user=os.environ['SQL_USER'],
                             host=os.environ['SQL_HOST'],
                             port=os.environ['SQL_PORT'],
                             password=os.environ['SQL_PASSWORD'],
                             autocommit=True) as conn:
            cur = conn.cursor()

            # Run query
            cur.execute("""SELECT study_id FROM podm_study
                           WHERE study = %(study)s AND pi = %(pi)s""",
                        {'study':study,'pi':pi})

            # Fetch value
            value = cur.fetchall()

            # Close cursor and database connection
            cur.close()
            conn.close()

            # return Value
            return(value[0][0])

    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def getMediumId(medium):
    ''' This function queries the podm_medium table for a medium_id
        related to a medium
        Parameters
            medium: string
                A medium type (e.g. water, dust, blood)
        Returns
            A medium_id value
    '''
    try:
        # Create connection to database, set autocommit, and get cursor
        with psycopg.connect(dbname=os.environ['SQL_DATABASE'],
                             user=os.environ['SQL_USER'],
                             host=os.environ['SQL_HOST'],
                             port=os.environ['SQL_PORT'],
                             password=os.environ['SQL_PASSWORD'],
                             autocommit=True) as conn:
            cur = conn.cursor()

            # Run query
            cur.execute("""SELECT medium_id FROM podm_medium
                           WHERE medium = %(medium)s""",
                        {'medium':medium})

            # Fetch value
            value = cur.fetchall()

            # Close cursor and database connection
            cur.close()
            conn.close()

            # return Value
            return(value[0][0])

    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def getTechniqueId(measurement):
    ''' This function queries the podm_tachnique table for a technique_id
        related to a measurement
        Parameters
            measurement: string
                A measurement type (e.g. Water Sample, Dust Sample, Serum Sample)
        Returns
            A technique_id value
    '''
    try:
        # Create connection to database, set autocommit, and get cursor
        with psycopg.connect(dbname=os.environ['SQL_DATABASE'],
                             user=os.environ['SQL_USER'],
                             host=os.environ['SQL_HOST'],
                             port=os.environ['SQL_PORT'],
                             password=os.environ['SQL_PASSWORD'],
                             autocommit=True) as conn:
            cur = conn.cursor()

            # Run query
            cur.execute("""SELECT technique_id FROM podm_technique
                           WHERE measurement = %(measurement)s""",
                        {'measurement':measurement})

            # Fetch value
            value = cur.fetchall()

            # Close cursor and database connection
            cur.close()
            conn.close()

            # return Value
            return(value[0][0])

    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def ingestSample(tableName,study,pi,measurement,medium,sgidcname):
    ''' This function inserts IDs into the podm_sample table which are then used to create
        a view with the other tables in the PFAS Observation Data Model
        Parameters
            tableName: string
                The name of the landing table that data will be pulled 
            study: string
                The study associated with the data (e.g. AHHS, ncsSerum, ncsDust)
            pi: string
                The name of the PI associated with the data (e.g. HUD, EPA)
            measurement: string
                The measurement associated with the data (e.g. Water Sample, Dust Sample, Serum Sample)
            medium: string
                The medium the sample was taken from (e.g. water, dust, blood)
            sgidcname: string
                The sample group column name (e.g. water_sample_id, dust_sample_id, serum_sample_id) 
        Returns
            Inserts ID's into the podm_sample table
    '''

    # Run the function getStudyId() to get the studyId
    studyId = getStudyId(study,pi)

    # Run the function getTechniqueId() to get the techniqueId
    techniqueId = getTechniqueId(measurement)

    # Rund the function getMediumId() to get the mediumId
    mediumId = getMediumId(medium)

    # Insert ID's into the podm_sample table. 
    insertSample(tableName,studyId,techniqueId,mediumId)

    # Update group ID's in the podm_sample table, where they are available
    addGroupId(sgidcname,mediumId)

    # If AHHS data update location ID in the podm_sample table
    if study == 'AHHS':
        addLocationId(sgidcname,mediumId)

def main(args):
    ''' Main program function takes args as input and runs specified task.
        Parameters
            args: dictionary
                contains the parameters listed below.
        Returns
            None
    '''

    # Get input arguments
    landingtablename = args.landingTableName
    study = args.study
    pi = args.pi
    measurement = args.measurement
    medium = args.medium
    sgidcname = args.sgidcname

    # Run the ingestSample() function
    ingestSample(landingtablename,study,pi,measurement,medium,sgidcname)

# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            landingTableName: string
                The landing table name (e.g. landing_ahhs_dust_data, landing_ahhs_water_data
                landing_ncsdust_data, landing_ncsserum_data)
            study: string
                The name of the study.
            pi: string
                "The name of the PI. 
            measurement: string
                The type of measurement.
            medium: string
                The type of medium.
            sgidcname: string
                The sample group column name.
        Returns
            None 
    '''

    # Defind parser
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--landingTableName", help="The landing table name", action="store", dest="landingTableName", required=True)
    parser.add_argument("--study", help="The name of the study", action="store", dest="study", required=True)
    parser.add_argument("--pi", help="The name of the PI", action="store", dest="pi", required=True)
    parser.add_argument("--measurement", help="The type of measurement", action="store", dest="measurement", required=True)
    parser.add_argument("--medium", help="The type of medium", action="store", dest="medium", required=True)
    parser.add_argument("--sgidcname", help="The sample group column name", action="store", dest="sgidcname", required=True)

    # Parse arguments
    args = parser.parse_args()

    # Run main
    main(args)

