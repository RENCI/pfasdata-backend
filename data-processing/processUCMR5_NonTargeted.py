#!/usr/bin/env python
# coding: utf-8
                
# import modules
import pandas as pd
import argparse


def main(args):
    ''' Main program function takes args as input and runs specified task.
        Parameters
            args: dictionary
                contains the parameters listed below.
        Returns
            None
    '''

    # Get input arguments
    inPath = args.inPath
    outPath = args.outPath
    inFile = args.inFile
    outFile = args.outFile
   
    # Read original non targeted data file 
    dfOrg = pd.read_csv(inPath+inFile)

    # exract column names
    columns = list(dfOrg.columns)
    columns.remove('sample_id')

    # put columns into lists
    colConcCurrent = []
    colConcFinal = []
    colMrlCurrent = []
    for column in columns:
        cparts = column.split('_')
        if cparts[1] == 'concentration':
            colConcCurrent.append(column)
            colConcFinal.append(cparts[0])
        elif cparts[1] == 'mrl':
            colMrlCurrent.append(column)

    # Put column names and variables in list for exploding
    refactored = []
    for index, row in dfOrg.iterrows():
        refactored.append([row.values[0],colConcFinal,row[colMrlCurrent].values.tolist(),
                           row[colConcCurrent].values.tolist()])
    
    # Convert list to DataFrame
    dfNew = pd.DataFrame(refactored, columns=['sample_id', 'pfas_short_name', 'mrl', 'measurement'])

    # Explode DataFrame
    dfNew = dfNew.explode(['pfas_short_name', 'mrl', 'measurement'])

    # Write DataFrame to CSV file
    dfNew.to_csv(outPath+outFile, index=False)

# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            inPath: string
                The directory path to the original non targeted data file.
            outPath: string
                The directory path to the reordered non targeted data file.
            inFile: string
                The file name of the original non targeted data. 
        Returns
            None
    ''' 

    # Defind parser 
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inPath", help="The directory path to the original non targeted data file", action="store", dest="inPath", required=True)
    parser.add_argument("--outPath", help="The directory path to the reordered non targeted data file", action="store", dest="outPath", required=True)
    parser.add_argument("--inFile", help="The file name of the original non targeted data", action="store", dest="inFile", required=True)
    parser.add_argument("--outFile", help="The file name of the processed non targeted data", action="store", dest="outFile", required=True)
        
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               
