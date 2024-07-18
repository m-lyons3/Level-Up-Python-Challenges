# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:21:35 2024

@author: Maria Lyons

Finding Palindromes of words

"""

"""
findPalindrome
Checks to see a word is a palindrome, or same forwards and backwards spelled. 
@param: Word to find palindrome of 
@return: True if the word is a palindrome. False otherwise


"""

def findPalindrome(word: str):
    backwards = ''
    
    # Removes spaces in a string
    word = word.replace(" ", '')
    
    # Makes all words lower case (so letter case doesn't matter)
    word = word.lower()
    
    length = len(word) - 1
    
    # Builds given word backwards
    while length >= 0:
        backwards = backwards + word[length]
        length -= 1
    print(f'Word given: {word}')
    print(f'Word backwards: {backwards}')
    return word == backwards


inputStr = input('Check palindrome of word: ')

# Checks if all characters are alphabetic
if all(char.isalpha() for char in inputStr):
    print(findPalindrome(inputStr))
else:
    print("Please refrain from using non-alphabetic characters!")

    
        
    
