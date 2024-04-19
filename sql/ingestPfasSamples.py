import os
import pandas as pd
import psycopg
import argparse
from dotenv import find_dotenv
from dotenv import load_dotenv

env_file = find_dotenv(".env.dev")
load_dotenv(env_file)
env_file = find_dotenv(".env.db.dev")
load_dotenv(env_file)

def insertSample(studyId,mediumId,locationId,techniqueId,sample):
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
            cur.execute("""INSERT INTO podm_sample(study_id, medium_id, location_id, technique_id, sample)
                           VALUES (%(studyid)s, %(mediumid)s, %(locationid)s, %(techniqueid)s,%(sample)s)""",
                        {'studyid':studyId,'mediumid':mediumId,'locationid':locationId,
                         'techniqueid':techniqueId,'sample':sample})

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

def getLocationId(zipcode):
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
            cur.execute("""SELECT location_id FROM podm_location
                           WHERE zipcode = %(zipcode)s""",
                        {'zipcode':zipcode})

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

def ingestSample(inputDir, inputFile):
    df = pd.read_csv(inputDir+inputFile)
    
    for index, row in df.iterrows():
        # sample,study,pi,measurement,units,medium,city,state,zipcode
        sample = row['sample']
        study = row['study']
        pi = row['pi']
        measurement = row['measurement']
        units = row['units']
        medium = row['medium']
        city = row['city']
        state = row['state']
        zipcode = row['zipcode']
        
        
        studyId = getStudyId(study,pi)
        mediumId = getMediumId(medium)
        locationId = getLocationId(zipcode)
        techniqueId = getTechniqueId(measurement)
        
        #print('study_id',str(studyId),'medium_id',str(mediumId),'location_id',str(locationId),
        #      'technique_id',str(techniqueId))
        insertSample(studyId,mediumId,locationId,techniqueId,sample)

def main(args):
    inputDir = args.inputDir
    inputFile = args.inputFile

    ingestSample(inputDir, inputFile)

# Run main function 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inputDir", help="Input directory path to data file", action="store", dest="inputDir", required=True)
    parser.add_argument("--inputFile", help="Input file name", action="store", dest="inputFile", required=True)

    # Parse arguments
    args = parser.parse_args()

    # Run main
    main(args)

