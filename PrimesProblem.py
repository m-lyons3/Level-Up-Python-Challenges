# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:18:05 2024

@author: Maria lyons

Finds the prime factorization of a given number.

"""

"""
findPrimes
Finds all the prime numbers up to the given number
@param num: The integer the function will find the primes up to
@return primeList: Returns the list of primes

"""
def findPrimes(num: int):
    numList = list(range(3, num))
    
    primeList = [2]
    
    # Uses the Sieve of Eratosthenes...
    # Primes before the approximent square root of a number are
    # the only necessary calculations of dividing... if not divisible
    # with primes under its square root, it is prime itself.
    for num in numList:
        sqrRoot = num ** 0.5
        for prime in primeList:
            if num % prime == 0:
                break
            if prime > sqrRoot:
                primeList.append(num)
                break
    return primeList

"""
primeFactorization
Returns the prime factorization, or the lowest primes 
needed to multiple up to a given number
@param: num. Integer to find prime factorization
@return: List of prime numbers to multiply up to given integer

"""
def primeFactorization(num: int):
    primes = findPrimes(num)
    primeFactors = []
    
    # Iterates until the number inputted divided into 1
    while num > 1:
        # Divides given number by primes until fully divisible.
        for prime in primes:
            if num % prime == 0:
                # Factor appended if fully divisible
                primeFactors.append(prime)
                num = num / prime
                break
        # This will check if the given number is prime.
        # If it is, it will return itself into a list
        if len(primeFactors) == 0:
            primeFactors.append(num)
            break
    return primeFactors



numberInput = (int(input("Input number to find primes of: ")))
primeFactorization = primeFactorization(numberInput)
print(f'Prime factorization of {numberInput} is {primeFactorization}')


    
    