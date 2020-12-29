# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:46:28 2020

@author: Louis
"""

"""
Takes an integer input n and returns the list of all primes up to and 
including n.
"""
def sieveOfEratosthenes(n):
    numbers = [True for i in range(n+1)]
    primes = []
    p = 2
    while p**2 <= n:
        if numbers[p] == True:
            for i in range(p**2, n+1, p):
                numbers[i] = False
        p +=1
    for p in range(2, n+1):
        if numbers[p] == True:
            primes.append(p)
    return primes

def main():
    n=500
    print(sieveOfEratosthenes(n))
    return

main()