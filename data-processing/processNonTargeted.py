#!/usr/bin/env python
# coding: utf-8
                
# import modules
import pandas as pd
import argparse

def getColumnNames(columns):
    ''' This program processes the non targeted column names for using in the reorderNonTargeted() function.
        Parameter
           columns: list
               The column names from the original non tageted data file
        Returns
           DataFrame
    '''

    # Define new DataFrame to insert processed column names.
    dfCols = pd.DataFrame(columns=['org_name','long_name','short_name','org_flags','flags'])

    # Define i as 0
    i = 0

    # For loop through column names 
    for column in columns:
        # Add 1 to i for future iterations
        i = i + 1

        # Determine if column is a flags column
        if column.split('.')[0] == 'Flags':
            # If flags column defind new flags name without a number
            # This variable is never used.
            flags = 'flags'
        else:
            # If not a flags column get original column name and flags
            org_name = column
            org_flags = columns[i]

            # Split column on open parentheses
            parts = column.split('(')

            # If there are two parts
            if len(parts) == 2:
                # get long_name and short name from parts
                long_name = parts[0].strip()
                short_name = parts[1].split(')')[0].strip()
            else:
                # else get long_name from parts and define short_name as None
                long_name = parts[0].strip()
                short_name = 'None'
           
            # Define dictionary based on row values 
            dicrow = {'org_name': org_name, 'long_name': long_name, 'short_name': 
                      short_name, 'org_flags': org_flags, 'flags': 'flags'}

            # Append dictionary to dfCols DataFrame
            dfCols = dfCols._append(dicrow, ignore_index = True)

    return(dfCols)

def reorderNonTargeted(outPath, outFile, dfOrg, dfCols):
    ''' This program reorder the not targeted data for ingest into the data model.
        Parameters
            outPath: string
                The directory path to the reordered non targeted data file.
            outFile: string
                The file name of the reordered non targeted data.
            dfOrg: DataFrame
               DataFrame containing the original non targeted data.
            dfCols: DataFrame
               DataFrame container the processed column names from the original non targeted data.
         Returns
            CSV file is written to disk
    '''
    dfNew = pd.DataFrame(columns=['sample_id','short_name','long_name','flags','measurement'])

    for index, row in dfOrg.iterrows():
        sample = row['Sample']
        for cindex, crow in dfCols.iterrows():
            org_name = crow['org_name']
            org_flags = crow['org_flags']
            short_name = crow['short_name']
            long_name = crow['long_name']
            flags = row[org_flags]
            measurement = row[org_name]
        
            dfrow = {'sample_id': sample, 'short_name': short_name, 'long_name': long_name,
                     'flags': flags, 'measurement': measurement}
            dfNew = dfNew._append(dfrow, ignore_index = True)
 
    dfNew.to_csv(outPath+outFile, index=False)


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
    outFile = "Model".join(inFile.split('Column'))
   
    # Read original non targeted data file 
    dfOrg = pd.read_csv(inPath+inFile)

    # exract column names
    columns = list(dfOrg.columns)
    columns.remove('Sample')

    # Process column names 
    dfCols = getColumnNames(columns)

    # Reorder non tageted data and output as new CSV file
    reorderNonTargeted(outPath, outFile, dfOrg, dfCols)

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
        
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               
