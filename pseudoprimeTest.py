# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:09:27 2020

@author: Louis
"""

"""
This takes an input integer 'n' and puts it through a pseudoprime test.
By Fermat's little theorem we know that a prime 'p' has the following property:
a^(p-1) is congruent to 1(mod p) for an integer 'a' coprime to 'p'.
We replace 'p' above with the potentially composite integer 'n', if it holds 
for the first few primes in place of 'a' then it is incredibly likely that 'n' 
is prime. The more primes that we use in place of 'a', the more likely that
the solution is correct.
"""
def pseudoprimeTest(n):
    if 2**(n-1)%n !=1 or 3**(n-1)%n !=1 or 5**(n-1)%n !=1 or 7**(n-1)%n !=1:
        print(str(n) + ' is composite.')
    else:
        print(str(n) + ' is probably prime.')
    return

def main():
    n = 523
    pseudoprimeTest(n)
    return

main()