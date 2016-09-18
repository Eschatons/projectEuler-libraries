# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:43:30 2016

@author: efron
"""
import numpy as np
import random
from typing import List

def sieve(n:int) -> List[int]:
    ''' uses sieve of erasthenes to produce primes under n '''
    if n < 2:
        return None
    isPrime = np.ones(n, dtype = bool)
    isPrime[0:2] = False
    isPrime[4::2] = False
    for p in range(3, n):
        if isPrime[p]:
            isPrime[p*2::p] = False
    return np.nonzero(isPrime)


def miller_rabin_primality(n:int) -> bool:
    ''' stochastic test for primality.
    True --> n is likely prime
    False --> n is definitely non-prime
    '''
    # based off https://inventwithpython.com/rabinMiller.py
    s = n-1
    t = 0
    while t % s == 0:
        s //= 2
        t += 1
        
    for trials in range(5):
        a = random.randrange(2, n-1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != n-1:
                if i == t-1:
                    return False
                else:
                    i += 1
                    v = (v**2) % n
    return True
    
def is_prime(n: int) -> bool:
    '''stochastically tests whether n is prime via trial divison of primes < 1000, 
    then the miller-rabin primality test. based off https://inventwithpython.com/rabinMiller.py
    True --> n is likely prime
    False --> n is definitely non-prime
    '''
    if n < 2:
        return False
    
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 
                 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 
                 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 
                 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
                 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
                 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
                 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    
    if n in lowPrimes:
        return True
    for prime in lowPrimes:
        if n % prime == 0:
            return False
    else:
        return miller_rabin_primality(n)
    

    # based off https://inventwithpython.com/rabinMiller.py