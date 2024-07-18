# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:48:53 2024

@author: Maria Lyons

Item Index Problem

Note: I actually solved this problem incorrectly, and marked where the key was with a '1'
and if not, there was a '0' placed there. Instead, it's supposed to mark the location
of the key depending on how many lists deep it was... I will revisit and some other point

"""
"""
itemLocation
Finds and marks the location of a key of the user's choice with a 1, otherwise 0
@param itemList: list to be iterated through
@param key: Integer that is being search and marked for
@return: list of items with the indeces marked if the key is there or not

"""

def itemLocation(itemList, key):
    itemIndex = itemList.copy()
    for index, item in enumerate(itemList):
        if isinstance(item, list):
            # Calls recursively, to check nested lists.
            itemIndex[index] = itemLocation(item, key)
        else:
            if item == key:
                itemIndex[index] = 1
            else:
                itemIndex[index] = 0
    return itemIndex
                
                



items = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(itemLocation(items, 2))