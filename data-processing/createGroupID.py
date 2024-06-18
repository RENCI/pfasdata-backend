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
            Writes DataFrame to CSV file
    '''

    # Get input arguments
    inLocPath = args.inLocPath
    inCrossPath = args.inCrossPath
    outputPath = args.outputPath
    inLocFile = args.inLocFile
    inCrossFile = args.inCrossFile

    # Read location file to DataFrame
    dfloc = pd.read_csv(inLocPath+inLocFile)

    # Drop City, State, Zipcode, and NaN values from DataFrame
    dfloc.drop(columns=['City', 'State', 'Zipcode'],inplace=True)
    dfloc.dropna(inplace=True)
    
    # Rename specified columns
    dfloc.rename(columns={'WaterSampleID': 'water_sample_id', 'DustSampleID': 'dust_sample_id'},inplace=True)

    # Change serum_sample_id to string
    dfloc['serum_sample_id'] = pd.Series(dtype='str')

    # Read crosswalk file to DataFrame 
    dfcross = pd.read_csv(inCrossPath+inCrossFile)

    # Drop Serum sampleid from DataFrame
    dfcross.drop(columns=['Serum sampleid'],inplace=True)

    # Rename specified columns
    dfcross.rename(columns={'Serum corrected sampleid': 'serum_sample_id', 'Dust sampleid': 'dust_sample_id'},inplace=True)

    # Change water_sample_id ti string
    dfcross['water_sample_id'] = pd.Series(dtype='str')

    # Subset Dataframe to specified columns
    dfcross = dfcross[['water_sample_id','dust_sample_id', 'serum_sample_id']]

    # Concatenate dfloc and dfcross DataFrames
    dfall = pd.concat([dfloc, dfcross], ignore_index=True, sort=False)

    # Write dfall DataFrame to csv file
    dfall.to_csv(outputPath+'sampleGroups.csv', index=False)

# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            inLocPath: string
                The directory path to the original location data file.
            inCrossPath: string
                The directory path to the original crosswalk data file.
            outputPath: string
                The directory path to the sample groups data file.
            inLocFile: string
                The file name of the location data file. 
            inCrossFile: string
                The file name of the crossewalk data file.
        Returns
            None
    ''' 

    # Defind parser 
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inLocPath", help="The directory path to the original location data file", action="store", dest="inLocPath", required=True)
    parser.add_argument("--inCrossPath", help="The directory path to the original crosswalk data file", action="store", dest="inCrossPath", required=True)
    parser.add_argument("--outputPath", help="The directory path to the sample groups data file", action="store", dest="outputPath", required=True)
    parser.add_argument("--inLocFile", help="The file name of the location data file", action="store", dest="inLocFile", required=True)
    parser.add_argument("--inCrossFile", help="The file name of the crossewalk data file", action="store", dest="inCrossFile", required=True)
 
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               

