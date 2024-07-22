# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:17:17 2024

@author: Maria Lyons

Dictionary Problem: Saves a dictionary into a JSON files and retrieves it
"""

import json

fruit = { 
    'a' : 'apple',
    'b' : 'banana',
    'c' : 'cantelope'
    }

"""
writeDict
Writes the dictionary to a json file 
@param dictionary: the dictionary to be written
@param fileName: the filename the dictionary will be written to

"""
def writeDict(dictionary, fileName):
    with open(fileName, 'w') as file:
        json.dump(dictionary, file)
        print('Data successfully written')
    
    
"""
readFromJson
Reads a dictionary from a json file and returns it
@param fileName: the file that will be read from
@return data: the dictionary to be returned

"""
def readFromJSON(fileName):
    try:
        with open(fileName, 'r') as file:
            data = json.load(file)
            print('Data extraction successful')
            return data
    except:
        print('Data extraction unsuccessful')
        
        
writeDict(fruit, 'dictionary.json')
print(readFromJSON('dictionary.json'))

