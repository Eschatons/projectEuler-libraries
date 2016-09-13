# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:44:35 2016

@author: efron
"""
from math import factorial as fact
from itertools import takewhile
from bisect import insort

def assert_int(*args):
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError('''
            argument should be an int, but is {0}
            '''.format(type(arg)))
    return None

def assert_non_negative(*args):
    for arg in args:
        if arg < 0:
            raise(ValueError('''
            argument should be greater than zero, but is {0}
            '''.format(arg)))


def n_choose_k(n: int, k: int) -> int:
    """ count of sets of k elements drawn from n unique objects without
    replacement. for sets with replacement, see multisets(n, k)
    """
    assert_int(n, k)
    assert_non_negative(n, k)
    def partial_factorial(n, k):
        total = 1
        for t in range(n, k, -1):
            total *= t
        return total
    if k > n:
        return 0
    k = max(k, n-k)
    return partial_factorial(n, k)//fact(n-k)


def permutations(n:int, k=None) -> int:
    """ number of orderings of k objects from a set of n unique objects.
    defaults to # of permutations of n objects. i.e,
    2-permutations of 'abc'
        ('ab', 'ac', 'bc')
    """
    if k is None:
        k = n
    assert_non_negative(n, k)
    assert_int(n, k)
    if k > n:
        return 0

    return fact(n) // fact(n-k)

def unique_permutations(*args):
    """ unique permutations of sequeneces of nonunique objects.
    arguments should be the number of unique objects of each kind.
    EG:
    we want permutations of ('aaabbbbcc'):
    --> a, b, c = 3, 4, 2
    >> count_permutations_of_nonunique_objects(a, b, c)
    """
    numerator = fact(sum(args))
    denominator = sum(fact(n) for n in args)
    return numerator // denominator

def multisets(n: int, k: int) -> int:
    """ count of multisets drawn from n unique elements with replacement.
    for sets with replacmenet, see multisets(n, k).
    """
    N = n+k-1
    return n_choose_k(N, k)


# stirling and bell numbers
def _make_stirling2():
    """ factory function that produces stirling2"""
    seen = {(0, 0): 1}
    def stirling2(n: int, k: int) -> int:
        """ S(n, k). stirling number of the second kind. this is the number
        of partitions of n distinct objects into k identical boxes. """
        nonlocal seen
        if (n, k) in seen:
            return seen[n, k]
        if k > n:
            return 0

        seen[n, k] = stirling2(n-1, k-1)+k*stirling2(n-1, k)
        return seen[n, k]

    return stirling2

stirling2 = _make_stirling2()

def _make_signless_stirling1():
    """ factory function that produes signless_stirling1 """
    seen = {(0, 0): 1}
    def signless_stirling1(n, k):
        """ c(n, k) = number of n-permutations with  k-cycles."""
        nonlocal seen
        if (n, k) in seen:
            return seen[n, k]
        if k == 0 or k > n:
            return 0
        a = signless_stirling1(n-1, k-1)
        b = (n-1) * signless_stirling1(n-1, k)
        return a + b
    return signless_stirling1

signless_stirling1 = _make_signless_stirling1()

def stirling1(n, k):
    """ stirling # of the first kind. c(n, k) = -1**(n-k)*c(n, k),
    where c(n,k) = signless_stirling1"""
    if n-k % 2:
        return -signless_stirling1(n, k)
    else:
        return signless_stirling1(n, k)

def bell(n):
    """ all set partitions of [n] into nonempty parts """
    if n == 0:
        return 1
    return sum(stirling2(n, k) for k in range(0, n+1))

# compositions
def compositions(n: int, k: int) -> int:
    return n_choose_k(n-1, k-1)

def all_compositions(n: int) -> int:
    return 1 << n


def weak_compositions(n: int, k: int) -> int:
    return n_choose_k(n+k-1, k-1)

# functions
def functions(n: int, k: int) -> int:
    return k ** n

def surjections(n: int, k: int) -> int:
    return stirling2(n, k)*fact(k)

def all_surjections(n: int) -> int:
    return sum(surjections(n, k) for k in range(1, n+1))

# set partitions
set_partitions = stirling2
all_set_partitions = bell
def weak_set_partitions(n, k):
    return sum(set_partitions(n, i) for i in range(1, k+1))


# integer partitions

def gen_pentagons():
    pentagonal = lambda n: (n*((3*n)-1)) // 2
    n = 1
    while True:
        n += 1
        yield pentagonal(n)
        yield pentagonal(-n)

class IntegerPartitions:

    def __init__(self, maxElem: int = 10):
        self.maxElem = 3
        self._seen = {0: 1, 1: 1, 2:2}
        self._pentagon = gen_pentagons()
        self.pentagons = [1, 2]
        self._update_maxElem(maxElem)

    def __getitem__(self, key: int) -> int:
        if key > self.maxElem and isinstance(key, int):
            newMaxElem = key
            self._update_maxElem(newMaxElem)
        return self._seen[key]

    def __len__(self):
        return len(self._seen)

    def _update_pentagons(self):
        """ create list of pentagonal numbers smaller than maxElem"""
        self.pentagons[-1]
        while self.pentagons[-1] <= self.maxElem:
            insort(self.pentagons, next(self._pentagon))
            insort(self.pentagons, next(self._pentagon))



    def _update_maxElem(self, newMaxElem):
        self.maxElem, oldMaxElem = newMaxElem, self.maxElem
        self._update_pentagons()
        for n in range(oldMaxElem, newMaxElem+1):
            self.partition(n)

    def __contains__(self, key):
        raise(NotImplementedError('__contains__ is not defined for IntegerPartitions'))
        

    def partition(self, key: int):
        """ find partitions of n using pentagonal formula """
        pentagons = takewhile(lambda x: x <= key, self.pentagons)
        total = 0
        for i, pentagon in enumerate(pentagons):
            mod = i % 4
            if mod == 0 or mod == 1:
                total += self._seen[key-pentagon]
            else:
                total -= self._seen[key-pentagon]
        self._seen[key] = total

integer_partition = IntegerPartitions()


