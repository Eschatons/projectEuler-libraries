# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:11:15 2016

@author: efron
"""

""" factors.py contains the FactorizationDict class number of functions related to factorizing
integers """

from primes import sieve
from collections import Counter
from bisect import bisect
from math import sqrt, ceil
from numbers import Number
from typing import Iterable


def product(iterable: Iterable[Number]):
    total = 1
    for x in iterable:
        total *= x
    return total

class FactorizationDict:
    """FactorizationDicts hold factorizations of positive integers.
    They allow for the speedy calculation of many number-theoretic properties,
    such as gcd, lcm, totient, and so on. """
    def __init__(self, maxElem: int, fillFactorTree = False):
        self.maxElem = maxElem
        self.primes = sieve(maxElem)
        self._factors = {prime: Counter([prime]) for prime in self.primes}
        self._factors[1] = Counter([1])
        self.filledFactorTree = fillFactorTree
        self.ϕ = self.totient # alias for totient if you want to be fancy
        if fillFactorTree:
            self.fill_factor_tree()

        
    # magic methods
    def __getitem__(self, key: int) -> Counter:
        return self._factors[key]
    def __setitem__(self, key: int, factors: Counter) -> None:
        self._factors[key] = factors
    def __len__(self) -> int:
        return len(self._factors)
    def __iter__(self) -> Iterable:
        return iter(self._factors)
    def __contains__(self, key: int) -> bool:
        return key in self._factors
    
    def __eq__(self, other) -> bool:
        return self._factors == other._factors

    def __str__(self) -> str:
        return str(self._factors)
    def __repr__(self) -> str:
        return 'FactorizationDict(maxElem = {0}, fillFactorTree = {1})'.format(
        self.maxElem, self.filledFactorTree)
        
    # non-magic methods
    def fill_factor_tree(self) -> None:
        """ precomputes entire factorization tree. this is somewhat optimized
        since we can create each number from it's factorization. """
        root = ceil(sqrt(self.maxElem))
        index = bisect(self.primes, max(3, root))
        for prime in self.primes[:index]:
            n = 2
            while prime*n < self.maxElem:
                self[prime*n] = self.factor(prime) + self.factor(n)
                n += 1
    def factor(self, n: int) -> int:
        """ factor an element into prime powers. saves intermediate results
        using dynamic programming. i.e, factor(125) will save factorizations
        of 5, 25, and 125 in order to make faster lookups later. """
        if n > self.maxElem:
            raise ValueError('''cannot factor element larger than 
                                largest prime in FactorizationDict!''')
        elif n < 1:
            raise ValueError('cannot factor zero, or negative numbers')
            
        if n in self:
            return self[n]
        for prime in self.primes:
            if n % prime == 0:
                factorization = self.factor(prime) + self.factor(n//prime)
                self[n] = factorization
                return factorization
                
    def totient(self, n: int) -> int:
        """ calculates euler's totient, ϕ(n), the number of integers
        1 < k < n such that gcd(k, n) == 1 """
        
        if n == 1:
            return 0
        if n < 1:
            raise(ValueError('no ϕ(n) for negative numbers!'))
        total = 1
        factors = self[n]
        for x in factors:
            total *= x**factors[x]-x**(factors[x]-1)
        return total
    
    
    def gcd(self, n: int, m: int) -> int:
        """ find greatest common divisor of n and m.
        i.e, find maximum d: d%n == 0 and  d%m == 0 """     
        if n == 0 or m == 0:
            raise ZeroDivisionError('no GCDs with zero!')
        n, m = abs(n), abs(m)
        sharedPrimes = self[n] & self[m]
        if len(sharedPrimes) > 0:
            return product(prime**sharedPrimes[prime] for prime in sharedPrimes)
        else:
            return 1
    
    def lcm(self, n: int, m: int) -> int:
        """ find least common multiple of n and m.
        i.e, find minimum k such that k = an = bm, a>=1, b>= 1
        """
        if n == 0 or m == 0:
            raise ZeroDivisionError('no LCMs with zero!')
        n, m = abs(n), abs(m)
        greaterPrimePowers = self[n] | self[m]
        return product(prime**greaterPrimePowers[prime] 
                for prime in greaterPrimePowers)
    
    def relatively_prime(self, n: int, m: int) -> bool:
        """ two numbers are relatively prime if gcd(n, m) == 1 """
        return self.gcd(n, m) == 1
    
    def multiplicative_group_mod_n_base_k(self, n: int, k: int=1) -> tuple:
        seen = []
        for prime in self.primes:
            if self.relatively_prime(prime, k):
                break
        while n not in seen:
            seen.append(n)
            n*= prime
        return tuple(seen)
    
            