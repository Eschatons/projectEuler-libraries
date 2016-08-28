# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:32:20 2016

@author: efron
"""

# tests for factor.py
from factor import FactorizationDict, product
from random import randint
from bisect import bisect
def test_factorization(F: FactorizationDict) -> None:
    for n in F:
        F.factor(n)
        factors = F[n]
        m = product(prime**factors[prime] for prime in F[n])
        assert(m == n)
    print('test_factorization passed!')

def test_fill_factor_tree() -> None:
    F = FactorizationDict(5000, fillFactorTree=False)
    G = FactorizationDict(5000, fillFactorTree=True)
    for n in range(1, F.maxElem):
        F.factor(n)
    assert(F == G)
    print('test_fill_factor_tree passed!')
def test_repr(F: FactorizationDict) -> None:
    G = eval(repr(F))
    assert(F == G)
    print('test_repr passed!')
    
def test_totient(F: FactorizationDict) -> None:
    def slow_ϕ(n: int) -> int:
        total = 0
        for m in range(1, n):
            if F.gcd(n, m) == 1:
                total += 1
        return total
    for n in range(50):
        k = randint(1, F.maxElem)
        slowϕ = slow_ϕ(k)
        fastϕ = F.ϕ(k)
        try:
            assert(slow_ϕ(k) == F.ϕ(k))
        except Exception as err:
            print(slowϕ)
            print(fastϕ)
            raise
    print('test_totient passed!')
def test_gcd(F: FactorizationDict) -> None:
    def slow_gcd(a: int, b: int) -> int:
        a, b = abs(a), abs(b)
        c = min(a, b)
        if b % c == 0 and a % c == 0:
            return c
        for d in range(max(a, b)//2, 0, -1):
            if b % d == 0 and a % d == 0:
                return d
        return 1
    for n in range(50):
        a, b= randint(1, F.maxElem), randint(1, F.maxElem)
        a *= -1**randint(1, 2)
        b *= -1**randint(1, 2)
        fastgcd = F.gcd(a, b)
        slowgcd = slow_gcd(a, b)
        try:
            assert(fastgcd == slowgcd)
        except Exception as err:
            print('a = {0}, b = {1}'.format(a, b))
            print(fastgcd)
            print(slowgcd)
            raise
    print('test_gcd passed!')
        
            
            
def test_lcm(F: FactorizationDict) -> None:
    def slow_lcm(a: int, b: int) -> int:
        a, b = abs(a), abs(b)
        m = max(a, b)
        d = m
        while d % b != 0 or d % a != 0:
            d += m
        return d
    for _ in range(50):
        a, b = randint(1, F.maxElem), randint(1, F.maxElem)
        a *= -1**randint(1, 2)
        b *= -1**randint(1, 2)
        fastlcm = F.lcm(a,b)
        slowlcm = slow_lcm(a,b)
        try:
            assert(F.lcm(a, b) == slow_lcm(a, b))
        except Exception as err:
            print('a = {0}, b = {1}'.format(a, b))
            print(fastlcm)
            print(slowlcm)
            raise
    
    print('test_lcm passed!')

def test_multiplicative_group_mod_n_base_k(F: FactorizationDict) -> None:
    print('test_multiplicative_group_mod_n_base_k not yet written')
    
def test_count_divisors(F: FactorizationDict) -> None:
    def find_divisors_slow(n: int) -> int:
        total = 0
        for m in range(1, n+1):
            if n % m == 0:
                total += 1
        return total
                
        
    for _ in range(30):
        n = randint(1, F.maxElem)
        fastD = F.count_divisors(n)
        slowD = find_divisors_slow(n)
        try:
            assert(fastD == slowD)
        except Exception as err:
            print('n = {0}'.format(n))
            print('count_divisors({0}) = {1}'.format(n, fastD))
            print('find_divisors_slow({0}) = {1}'.format(n, slowD))
    print('test_count_divisors passed!')
    

def run_all_tests():
    F = FactorizationDict(5000, fillFactorTree = True)            
    test_factorization(F)
    test_fill_factor_tree()
    test_repr(F)
    test_totient(F)
    test_gcd(F)
    test_lcm(F)
    test_multiplicative_group_mod_n_base_k(F)
    test_count_divisors(F)
    print('ALL TESTS PASSED!')
run_all_tests()