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

def insertSample(studyId,techniqueId,mediumId):
    ''' This function inserts IDs into the podm_sample table. Three of the IDs are inputs to this
        function (e.g. studyId,techniqueId,mediumId), two are set to single values and later updated
        (e.g. group_id, location_id), and one (i.e. study_id) is obtained from one of four landing 
        tables.
        Parameters             
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
                                                           location_id, technique_id, date)
                                       SELECT ucmr5.unique_id, %s, %s, %s, pl.location_id, %s, ucmr5.date
                                       FROM landing_usmr5_data ucmr5
                                       INNER JOIN podm_location pl ON pl.site_id=ucmr5.pwsid"""),
                                       [studyId, -9, mediumId, techniqueId])
                
            # Close cursor and database connection
            cur.close()
            conn.close()
            
    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def getStudyId(study):
    ''' This function queries the podm_study table for a study_id
        related to a study and pi
        Parameters
            study: string
                A study (UCMR5)
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
                           WHERE study = %(study)s""",
                        {'study':study})

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
	
def ingestSample(study,measurement,medium):
    ''' This function inserts IDs into the podm_sample table which are then used to create
        a view with the other tables in the PFAS Observation Data Model
        Parameters
            study: string
                The name of the study associated with the data (e.g. UCMR%, AHHS)
            measurement: string
                The measurement associated with the data (e.g. Water Sample, Dust Sample, Serum Sample)
            medium: string
                The medium the sample was taken from (e.g. water, dust, blood)
        Returns
            Inserts ID's into the podm_sample table
    '''

    # Run the function getStudyId() to get the studyId
    studyId = getStudyId(study)

    # Run the function getTechniqueId() to get the techniqueId
    techniqueId = getTechniqueId(measurement)

    # Rund the function getMediumId() to get the mediumId
    mediumId = getMediumId(medium)

    # Insert ID's into the podm_sample table. 
    insertSample(studyId,techniqueId,mediumId)

def main(args):
    ''' Main program function takes args as input and runs specified task.
        Parameters
            args: dictionary
                contains the parameters listed below.
        Returns
            None
    '''

    # Get input arguments
    study = args.study
    measurement = args.measurement
    medium = args.medium

    # Run the ingestSample() function
    ingestSample(study,measurement,medium)

# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            study: string
                "The name of the study. 
            measurement: string
                The type of measurement.
            medium: string
                The type of medium.
        Returns
            None 
    '''

    # Defind parser
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--study", help="The name of the study", action="store", dest="study", required=True)
    parser.add_argument("--measurement", help="The type of measurement", action="store", dest="measurement", required=True)
    parser.add_argument("--medium", help="The type of medium", action="store", dest="medium", required=True)

    # Parse arguments
    args = parser.parse_args()

    # Run main
    main(args)

