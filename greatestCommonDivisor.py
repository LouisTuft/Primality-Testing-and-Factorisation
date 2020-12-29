# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:22:52 2020

@author: Louis
"""

"""
Takes two integer inputs a,b and returns their greatest common divisor.
"""
def greatestCommonDivisor(a,b):
    while b != 0:
        z = b
        b = a%b
        a = z
    return a

def main():
    a = 32
    b = 72
    print(greatestCommonDivisor(a,b))
    return

main()