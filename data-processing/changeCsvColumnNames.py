#!/usr/bin/env python
# coding: utf-8

# import modules
import pandas as pd
import argparse

def changeCsvColumnNames(inputPath,outputPath,fileName):
    # read input file as DataFrame
    df = pd.read_csv(inputPath+fileName)
    
    # define columns as a dictionary
    columns = {}
    
    # loop through columns and remove (ng/mL) and change to lower case
    for column in df.columns:
        if fileName == 'NCSSerum_output_Column_Corrected_SampleID.csv':
            if column.lower() == 'correctsampleid':
                columns[column] = 'sample_id'
            else:
                columns[column] = column.split('.')[0].lower()
        else:
            if column.lower() == 'sample':
                columns[column] = 'sample_id'
            else:
                columns[column] = column.split('(')[0].lower()

    # add revized colunm names to DataFrame
    df = df.rename(columns=columns)
    df.to_csv(outputPath+fileName, index=False)

def main(args):
    ''' Main program function takes args as input and runs specified task.
        Parameters
            args: dictionary
                contains the parameters listed below.
        Returns
            None
    '''

    # Get input arguments
    inputPath = args.inputPath
    outputPath = args.outputPath
    fileName = args.fileName

    # Run the changeCsvColumnNames() function   
    changeCsvColumnNames(inputPath,outputPath,fileName)


# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            inputPath: string
                The directory path to the original data file.
            outputPath: string
                The directory path to the column name corrected file.
            fileName: string
                The file name of the original data file. 
        Returns
            None
    ''' 

    # Defind parser 
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inputPath", help="The directory path to the original data file", action="store", dest="inputPath", required=True)
    parser.add_argument("--outputPath", help="The directory path to the column name corrected file", action="store", dest="outputPath", required=True)
    parser.add_argument("--fileName", help="The file name of the original data file", action="store", dest="fileName", required=True)
        
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               

