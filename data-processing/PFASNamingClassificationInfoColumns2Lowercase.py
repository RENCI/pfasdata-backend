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
    outFile = args.outFile

    # Convert encodding from utf-8 to cp1254 to read data
    file_encoding = 'cp1252'  # 'utf-8'

    # Read PFASNamingClassificationInformationShortCaps.csv into DataFrame and
    # change a cllumns to lower case
    df = pd.read_csv(inPath+inFile, encoding=file_encoding)
    df.columns = [x.lower() for x in df.columns]

    # Write DataFrame to CSV file
    df.to_csv(outPath+outFile, index=False)

# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            inPath: string
                The directory path to the original data files.
            outPath: string
                The directory path to the output lowercase data files.
            inFile: string
                The file name of the original data file. 
            outFile: string
                The file name of the lowercase output data file.
        Returns
            None
    ''' 

    # Defind parser 
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inPath", help="The directory path to the original data files", action="store", dest="inPath", required=True)
    parser.add_argument("--outPath", help="The directory path to the output lowercase data files", action="store", dest="outPath", required=True)
    parser.add_argument("--inFile", help="The file name of the original data file", action="store", dest="inFile", required=True)
    parser.add_argument("--outFile", help="The file name of the lowercase output data file", action="store", dest="outFile", required=True)
 
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               
