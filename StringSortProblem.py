# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:54:20 2024

@author: Maria Lyons

Organizing a string alphabetically
"""


class WordSort:
    
    def __init__(self, string):
        self.string = string
        
    """
    Overrides Magic Method to compare strings regardless of case
    """
    def __lt__(self, other):
        # Ensure that 'other' is a string before calling casefold
        if isinstance(other, str):
            return self.string.casefold() < other.casefold()
        else:
            return ("Not a String")
    
    """
    sortString
    Sorts the words in the string based on alphabetical order in the list
    @return: Returns the list of words in alphabetical order
    """
    def sortString(self):
        # Splits into a list, separated by spaces.
        listOfWords = self.string.split(" ")
    
        # Sorts words alphabetically, ignoring case
        # An attempt was done with using .sort() but did not work :(
        listOfWords = sorted(listOfWords, key=str.casefold)
        return " ".join(listOfWords)

sentence = WordSort("apple Orange BANANA")
print(sentence.sortString())
