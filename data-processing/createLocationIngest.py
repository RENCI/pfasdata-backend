#!/usr/bin/env python
# coding: utf-8

# import modules
import pandas as pd # Reading csv file
import argparse # Input arguments parser

def main(args):
    ''' Main program function takes args as input and runs specified task.
        Parameters
            args: dictionary
                contains the parameters listed below.
        Returns
            Writes SQL ingest data file to disk 
    '''

    # Get input arguments
    inPath = args.inPath
    sqlPath = args.sqlPath
    dustFile = args.dustFile
    waterFile = args.waterFile

    # Read in two input files as DataFrames
    dfd = pd.read_csv(inPath+dustFile, dtype={'Zipcode': 'str'})
    dfw = pd.read_csv(inPath+waterFile, dtype={'Zipcode': 'str'})

    # drop first column which pertains to the sample ID
    columns = dfd.columns
    dfd.drop(columns[0], inplace=True, axis=1)
    columns = dfw.columns
    dfw.drop(columns[0], inplace=True, axis=1)
    dfb = pd.concat([dfd, dfw], ignore_index=True)

    # get unique zipcodes
    zipcodes = list(dfb['Zipcode'].unique())

    # open output file for writing
    f = open(sqlPath+'insertLocation.sql', 'w')

    # write insert command and values command
    f.write('INSERT INTO podm_location (city, state, zipcode)\n')
    f.write('VALUES\n')

    # insert fill values for serum data
    f.write("('xxxx','xx','-99999'),\n")

    # count the number of zipcodes
    numzips = len(zipcodes)
    i = 0

    # loop through zipcodes
    for zipcode in zipcodes:
        # count iterations
        i = i + 1
    
        # extract unique city and state values for a specific zip code 
        city = dfb['City'].loc[dfb['Zipcode'] == zipcode].unique()[0]
        state = dfb['State'].loc[dfb['Zipcode'] == zipcode].unique()[0]
    
        # check if last iteration 
        if i != numzips:
            # write city, state, and zipcode values to output file and continue
            f.write("('"+str(city)+"','"+str(state)+"','"+str(zipcode)+"'),\n")
        elif i == numzips:
            # write city, state, and zipcode values to output file and stop
            f.write("('"+str(city)+"','"+str(state)+"','"+str(zipcode)+"');\n")
        else:
            # print message if numzip is not working properly
            print('Somethings up with numzips')

    # close output files
    f.close()

# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            inPath: string
                The directory path to the original dust and water data files.
            sqlPath: string
                The directory path to the output SQL data file.
            dustFile: string
                The file name of the dust location  data file. 
            waterFile: string
                The file name of the water location data file.
        Returns
            None
    ''' 

    # Defind parser 
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inPath", help="The directory path to the original dust and water data files", action="store", dest="inPath", required=True)
    parser.add_argument("--sqlPath", help="The directory path to the output SQL data file", action="store", dest="sqlPath", required=True)
    parser.add_argument("--dustFile", help="The file name of the dust data file", action="store", dest="dustFile", required=True)
    parser.add_argument("--waterFile", help="The file name of the water data file", action="store", dest="waterFile", required=True)
 
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               

