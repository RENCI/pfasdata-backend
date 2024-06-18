#!/usr/bin/env python
# coding: utf-8

# import modules
import pandas as pd # Reading csv file 
import argparse # Input arguments parser
from shapely import wkb, wkt # Well-known binary (WKB) and Well-known text (WKT)
from shapely.geometry import Point # Shapely for converting latitude/longtitude to geometry
import geopandas as gpd # To create GeodataFrame
from pyproj import CRS # Py Proj's Coordinate Reference System manager

def addGeom(inputPath,outputPath,inputFileName,outputFileName,lonName,latName):
    # read input file
    df = pd.read_csv(inputPath+inputFileName)
    
    # rename lon and lat columns to standard name
    df = df.rename(columns={lonName: 'longitude', latName: 'latitude'})
    
    # change all column names to lower case
    df.columns = [x.lower() for x in df.columns]

    # create Geometry
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    crs = CRS('EPSG:4326')
    gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

    # convert geometry to wkb
    geom = [wkb.dumps(wkt.loads(str(geom)), hex=True, srid=4326) for geom in df['geometry']]
    df['geom'] = geom
    df = df.drop('geometry', axis=1)
    df.to_csv(outputPath+outputFileName, index=False)

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
    inputFileName = args.inputFileName
    outputFileName = args.outputFileName
    lonName = args.lonName
    latName = args.latName

    # Run the addGeom() function   
    addGeom(inputPath,outputPath,inputFileName,outputFileName,lonName,latName)


# Run main function 
if __name__ == "__main__":
    ''' Takes argparse inputs and passes theme to the main function
        Parameters
            inputPath: string
                The directory path to the original data file.
            outputPath: string
                The directory path to the column name corrected file.
            inputFileName: string
                The file name of the original data file. 
            outputFileName: string
                The file name of the output data file.
            lonName: string
                The name of the longitude variable (e.g. long_final, lon, longitude)
            latName: string
                The name of the latitude variable (e.g. lat_final, lat, latitude)
        Returns
            None
    ''' 

    # Defind parser 
    parser = argparse.ArgumentParser()

    # None optional argument
    parser.add_argument("--inputPath", help="The directory path to the original data file", action="store", dest="inputPath", required=True)
    parser.add_argument("--outputPath", help="The directory path to the column name corrected file", action="store", dest="outputPath", required=True)
    parser.add_argument("--inputFileName", help="The file name of the original data file", action="store", dest="inputFileName", required=True)
    parser.add_argument("--outputFileName", help="The file name of the output data file", action="store", dest="outputFileName", required=True)
    parser.add_argument("--lonName", help="The name of the longitude variable (e.g. long_final, lon, longitude", action="store", dest="lonName", required=True)
    parser.add_argument("--latName", help="The name of the latitude variable (e.g. lat_final, lat, latitude)", action="store", dest="latName", required=True)
 
    # Parse arguments        
    args = parser.parse_args()
                             
    # Run main               
    main(args)               

