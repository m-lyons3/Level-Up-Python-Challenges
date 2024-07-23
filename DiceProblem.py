# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:52:29 2024

@author: Maria Lyons

Roll Dice Simulation: Takes in a certain amount of sided dice and the number
of trials the user wishes and finds the probability of each roll
based on the Monte Carlo method

"""

from random import randint
from collections import defaultdict

"""
diceRolls
Simulates a certain number of rolls given a certain amount of sided dice
@param *dice: Numbers that represent the amount of sides a dice has. Can input as many as user wishes
@param trialNum: How many times the user wishes the simulate dice rolls

"""
def diceRolls(*dice, trialNum):
    maxSum = sum(dice)
    rollSum = 0
    trial = 0
    
    # Sorts the roll sums into a dictionary to reference later
    rollCount = defaultdict(int)
    while trial < trialNum:
        for die in dice:
            roll = randint(1, die)
            rollSum += roll
        rollCount[rollSum] += 1
        trial += 1
        rollSum = 0
    sortedRolls = dict(sorted(rollCount.items()))
    # Finds the probability of each roll from given number of trials
    probabilityRolls(sortedRolls, trialNum)

"""
probabilityRolls
@param rolls: The dictionary contains the number of rolls per each value
@param trialNum: the number of trials the user wants to sample from

"""
def probabilityRolls(rolls, trialNum):
        probabilities = {key: value / trialNum for key, value in rolls.items()}
        # Prints the percentage of probability for each possible roll
        for key,value in probabilities.items():
            print(f'{key}: {round(value * 100, 2)}%')
        return
        
rolls = diceRolls(6, 4, 4, trialNum = 1000000)


        
        



