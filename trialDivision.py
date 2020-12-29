# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:40:10 2020

@author: Louis
"""

"""
A simple Trial Division algorithm. We use the SoE to generate a list of 
primes up to some 'limit', then we divide an integer 'n' by all the 
primes in that list and return the factors.
"""
def sieveOfEratosthenes(limit):
    numbers = [True for i in range(limit+1)]
    primes = []
    p = 2
    while p**2 <= limit:
        if numbers[p] == True:
            for i in range(p**2, limit+1, p):
                numbers[i] = False
        p +=1
    for p in range(2, limit+1):
        if numbers[p] == True:
            primes.append(p)
    return primes

def trialDivision(n,listOfPrimes):
    factors = []
    for i in range(len(listOfPrimes)):
        if n%listOfPrimes[i]==0:
            factors.append(listOfPrimes[i])
    return factors

def main():
    limit = 100
    listOfPrimes = sieveOfEratosthenes(limit)
    n = 787
    print('The factors of ' + str(n) + ' are: ' + 
          str(trialDivision(n,listOfPrimes)))
    return

main()