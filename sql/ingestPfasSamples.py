import os
import pandas as pd
import psycopg
from psycopg import sql
import argparse
from dotenv import find_dotenv
from dotenv import load_dotenv

env_file = find_dotenv(".env.dev")
load_dotenv(env_file)
env_file = find_dotenv(".env.db.dev")
load_dotenv(env_file)

def insertSample(landingTable,studyId,techniqueId,mediumId):
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
                                   WHERE ll.{sgidcname}=ps.sample_id
                                   AND ps.medium_id = %s 
                                   """).format(sgidcname=sql.Identifier(sgidcname)),
                                   [mediumId])                

                
            # Close cursor and database connection
            cur.close()
            conn.close()
            
    # If exception log error
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
	
def getStudyId(study,pi):
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
    studyId = getStudyId(study,pi)
    techniqueId = getTechniqueId(measurement)
    mediumId = getMediumId(medium)

    insertSample(tableName,studyId,techniqueId,mediumId)
    addGroupId(sgidcname,mediumId)

    if study == 'AHHS':
        addLocationId(sgidcname,mediumId)

def main(args):
    landingtablename = args.landingTableName
    study = args.study
    pi = args.pi
    measurement = args.measurement
    medium = args.medium
    sgidcname = args.sgidcname

    ingestSample(landingtablename,study,pi,measurement,medium,sgidcname)

# Run main function 
if __name__ == "__main__":
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

