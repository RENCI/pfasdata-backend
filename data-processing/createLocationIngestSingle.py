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
    outPath = args.outPath
    inFile = args.inFile

    # Read in two input files as DataFrames
    df = pd.read_csv(inPath+inFile, dtype={'Zipcode': 'str'})

    # drop first column which pertains to the sample ID
    columns = df.columns
    df.drop(columns[0], inplace=True, axis=1)

    # get unique zipcodes
    zipcodes = list(df['Zipcode'].unique())

    # open output file for writing
    f = open(outPath+inFile.split('.')[0]+'.sql', 'w')

    # write insert command and values command
    f.write('INSERT INTO podm_location (city, state, zipcode)\n')
    f.write('VALUES\n')

    # count the number of zipcodes
    numzips = len(zipcodes)
    i = 0

    # loop through zipcodes
    for zipcode in zipcodes:
        # count iterations
        i = i + 1
    
        # extract unique city and state values for a specific zip code 
        city = df['City'].loc[df['Zipcode'] == zipcode].unique()[0]
        state = df['State'].loc[df['Zipcode'] == zipcode].unique()[0]
    
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
            outPath: string
                The directory path to the output SQL data file.
            inFile: string
                The file name of the original location data file. 
        Returns
            None
    ''' 

    # Defind parser 
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inPath", help="The directory path to the original location data files", action="store", dest="inPath", required=True)
    parser.add_argument("--outPath", help="The directory path to the output SQL data file", action="store", dest="outPath", required=True)
    parser.add_argument("--inFile", help="The file name of the original location data file", action="store", dest="inFile", required=True)
 
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               

