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

            # Get study name and sample year from the podm_study table.
            cur.execute(sql.SQL("""SELECT study, year
                                   FROM podm_study
                                   WHERE study_id = %s"""),
                                   [studyId])
            
            value = cur.fetchall()
            study = value[0][0]
            sampleyear = int(value[0][1])
            
            # Run query
            cur.execute(sql.SQL("""INSERT INTO podm_sample(sample_id, study_id, group_id, medium_id, 
                                                           location_id, technique_id)
                                       SELECT usgs.id, %s, %s, %s, pl.location_id, %s
                                       FROM podm_pfas_in_tapwater_usgs usgs
                                       INNER JOIN podm_location pl ON pl.site_id=usgs.station_na
                                       WHERE usgs.study = %s AND usgs.sampleyear = %s"""),
                                       [studyId, -9, mediumId, techniqueId, study, sampleyear])
                
            # Close cursor and database connection
            cur.close()
            conn.close()
            
    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def getStudyId(pi):
    ''' This function queries the podm_study table for a study_id
        related to a study and pi
        Parameters
            pi: string
                A PI (USGS)
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
                           WHERE pi = %(pi)s""",
                        {'pi':pi})

            # Fetch value
            value = cur.fetchall()

            # Close cursor and database connection
            cur.close()
            conn.close()

            # return Value
            return(value)

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
	
def ingestSample(pi,measurement,medium):
    ''' This function inserts IDs into the podm_sample table which are then used to create
        a view with the other tables in the PFAS Observation Data Model
        Parameters
            pi: string
                The name of the PI associated with the data (e.g. HUD, EPA)
            measurement: string
                The measurement associated with the data (e.g. Water Sample, Dust Sample, Serum Sample)
            medium: string
                The medium the sample was taken from (e.g. water, dust, blood)
        Returns
            Inserts ID's into the podm_sample table
    '''

    # Run the function getStudyId() to get the studyId
    studyIds = getStudyId(pi)

    # Run the function getTechniqueId() to get the techniqueId
    techniqueId = getTechniqueId(measurement)

    # Rund the function getMediumId() to get the mediumId
    mediumId = getMediumId(medium)

    # Insert ID's into the podm_sample table. 
    for studyId in studyIds:
        insertSample(studyId[0],techniqueId,mediumId)

def main(args):
    ''' Main program function takes args as input and runs specified task.
        Parameters
            args: dictionary
                contains the parameters listed below.
        Returns
            None
    '''

    # Get input arguments
    pi = args.pi
    measurement = args.measurement
    medium = args.medium

    # Run the ingestSample() function
    ingestSample(pi,measurement,medium)

# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            pi: string
                "The name of the PI. 
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
    parser.add_argument("--pi", help="The name of the PI", action="store", dest="pi", required=True)
    parser.add_argument("--measurement", help="The type of measurement", action="store", dest="measurement", required=True)
    parser.add_argument("--medium", help="The type of medium", action="store", dest="medium", required=True)

    # Parse arguments
    args = parser.parse_args()

    # Run main
    main(args)

