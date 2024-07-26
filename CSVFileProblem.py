# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:51:18 2024

@author: Maria Lyons

Merging CSV files problem: Merges number of csv files together


"""

import pandas as pd

"""
mergeCSV
Merges number of csv files into one output file
@param: *csvFiles: number of csv files the user wants to merge
@param: the name of the file the csv files will merge into

"""
def mergeCSV(*csvFiles, outputFile):
    
    try:
        csvList = []
        for file in csvFiles:
            csvList.append(file)
        
        # Sorts all the csv files into pandas dataframes
        dataFrames = [pd.read_csv(file) for file in csvList]
    
        # Concatenates all the dataframes into one merged df
        mergedDf = pd.concat(dataFrames, ignore_index = True)
    
        # Converts the merged datafram into one csv file
        mergedDf.to_csv(outputFile, index = False)
    
        print(f'Combination successful. Saved to {outputFile}')
        
    except:
        print(f'Merger unsuccessful')
    
mergeCSV('csvFile1.csv', 'csvFile2.csv', 'csvFile3.csv', outputFile = 'output.csv')
        