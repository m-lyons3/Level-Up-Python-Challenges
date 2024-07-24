# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:32:42 2024

@author: Maria Lyons

Password Problem

"""
""" 
generatePassword
@param: number of words to include in new password
@return: a list of words in new password separated by spaces

"""

# Not truly random! Use secrets library documentation for future implementation
import random


"""
generatePassword
Generates a new password based on diceware txt file (using words instead of random characters)
@param: wordNum: number of words in password
@return: the new password
"""
def generatePassword(wordNum):
    # Each word is represented by a 5 number long integer, with
    # each slot being a number 1-6
    
    numStr = ''
    wordList = []
    
    # Finds list random numbers for generation of words
    for words in range(wordNum):
        for j in range(5):
            rand = str(random.randint(1, 6))
            numStr += rand
        wordList.append(numStr)
        numStr= ''
    print(f'String: {wordList}')
    
    # Opening diceware file with words and corresponding numbers
    with open('diceware.txt', 'r') as file:
        print('Opened file successfully')
        
        password = ''
        for line in file:
            parse = line.split()
            index = 0
            for code in (wordList):
                # To avoid unneccessary lines without number/word
                if len(parse) == 2:
                    number, word = parse
                    if number == code:
                        wordList[index] = word
                        print(f"Number: {number}, Word: {word}")
                index += 1
    password = ' '.join(wordList)
    return password

print(generatePassword(5))
