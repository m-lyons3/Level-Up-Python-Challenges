# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:27:39 2024

@author: Maria Lyons

The Waiting Game. Given a number of seconds, try to time it with the enter key!

"""
import random
import time

# Holds all the methods and functionality for the game
class WaitingGame:
    
    enterString = '------ Press Enter to Start Timer ------'
    directions = 'Given the number of seconds on the screen, try to time hitting the enter key as close to the number of seconds!'
     
    def __init__(self):
        # Starting dialogue. Only shows once
         print('Welcome to the Waiting Game!')
         time.sleep(1)
         print(self.directions)
         time.sleep(1)
         print('Are you ready?')
         time.sleep(2)
         
         self.startGame()
         
    """
    startGame
    Starts the waiting game, along with the recording of times to challenge the player
    
    """
    def startGame(self):
         print('')
         
         # Picks a random second between 1 and 7
         randSec = random.randrange(1, 7, 1)
         print(f'Your number of seconds is {randSec}.')
         input(self.enterString)
         
         # Time needed to stop on
         targetTime = time.time() + randSec
         input('Timer Started! Press Enter to Stop Timer.\n ')
         endTime = time.time()
         
         # Compares the times
         
         print('Timer Stopped! How Close Were You?\n')
         time.sleep(2)
         
         self.compareTimes(targetTime, endTime, randSec)
         
         self.playAgain()
         
    """
    compareTimes
    Compares the user's time and the actual time needed. 
    @param target: the target time
    @param end: The user's time
    @param numSec: the goal of seconds

    """    
    def compareTimes(self, target, end, numSec):
        difference = target - end
        if difference > 0:
            print(f'You were {difference} under the target time of {numSec}!')
        elif difference < 0:
            print(f'You were {difference * -1} over the target time of {numSec}!')
        else:
            print('WOW! Perfect! The difference was {difference}')
            
            
    """
    playAgain
    Asks the user if they will play again. They can choose to our quit the program
    
    """
    def playAgain(self):
         play = input('Do you want to play again? Y for yes. N for no: ' ).lower()
         if play == 'y':
             self.startGame()
         elif play == 'n':
             print('Thank you for playing!')
             return
         else:
             self.playAgain()
             
             

game = WaitingGame()
