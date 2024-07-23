# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:48:32 2024

@author: Maria Lyons

Total Words and word count of the top twenty frequent words
in a text file
"""

from operator import itemgetter
from collections import Counter

punctuation = [',', '\'', ';', '.' ':']


"""
wordCount
Counts the number of words and lists the 20 most common words with their count
from a text file.
@param: A textfile

"""
def wordCount(textFile):
    
    wordTracker = dict()
    wordNum = 0
    
    with open(textFile, 'r') as file:
        text = file.read()
        
        # Cleaning text 
        for symbol in punctuation:
            text = text.replace(symbol, '')
        wordList = text.lower().split(' ')
    
    # Creating a count of words and a dictionary for each word and their matching count
    for word in wordList:
        wordNum += 1
        if word.lower() not in wordTracker:
            wordTracker[word] = 1
        else:
            wordTracker[word] += 1
    
    # dict.items() returns a list of tuples with keys and their values. 
    # item[1] is the value, so the dictionary is sorted by its value
    sortedList = dict(sorted(wordTracker.items(), key=lambda item: item[1], reverse=True))
            
    # Lists the word count and 20 most common words
    print(f'Word count: {wordNum}')
    print('--- The 20 most common words in the text file ---')
    count = 1
    for key, value in sortedList.items():
        if count > 20:
            break
        count += 1
        print(f'Word: {key} ||| Count: {value}')
    return
    
print(wordCount('DeclarationOfIndependence.txt'))