# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:20:36 2016

@author: efron
"""
from numbers import Integral
import numpy as np
from collections import namedtuple
class PartitionCount:
    def __init__(self, maxElem, *, fillPartitionTree = True):

                
        self.maxElem = maxElem
        self._partitions = {0: 1, 1:1, 2:2, 3:2}
        self.filledPartitionTree = fillPartitionTree
        self.pentagonals = self._initalize_pentagonals()
        if self.filledPartitionTree:
            for n in range(1, maxElem):
                self.count_partitions(n)
        
    def __len__(self, n):
        return len(self._partitions)
    
    def __getitem__(self, n):
        if not isinstance(n, Integral):
            raise KeyError('partitions only defined for integers')
        try:
            return self._partitions[n]
        except KeyError:
            return self.count_partitions(n)
    
    def __iter__(self, n):
        return iter(self._partitions)
        
    def __contains__(self, x) -> bool:
        return x in self._partitions
        
    def __eqs__(self, other):
        return self._partitions == other._partitions
    
    def count_partitions(self, n : int) -> int:
        def partitions_of_pentagonal_children(n: int) -> int:
            childSum = 0
            
            def sign(pentagon):
                if (pentagon.index-1) % 2:
                    print(pentagon)
                    return -1
                else:
                    print(pentagon)
                    return 1
                
            for pentagon in self.pentagonals:
                k = pentagon.value
                if k > n:
                    break
                else:
                    if n == 5:
                        print(childSum)
                        print('n = {0}'.format(n))
                        print('k = {0}'.format(k))
                        print('p(n-k) = {0}'.format(self._partitions[n-k]))
                    childSum += sign(pentagon)*self._partitions[n-k]


            return childSum
        if n < 0:
            return 0
        elif n in self:
            return self[n]
        else:
            self._partitions[n] = partitions_of_pentagonal_children(n)
            return self[n]
        
    def _initalize_pentagonals(self):
        pentagon = namedtuple('Pentagon', ['value', 'index'])
        pentagonal = lambda n: (n*(3*n-1)) // 2
        n = 1
        pentagonals = []
        positivePentagonal = pentagonal(n)
        negativePentagonal = pentagonal(-n)
        while positivePentagonal <= self.maxElem:
            pentagonals.append(pentagon(positivePentagonal, n))
            pentagonals.append(pentagon(negativePentagonal, -n))
            n += 1
            positivePentagonal = pentagonal(n)
            negativePentagonal = pentagonal(-n)
        pentagonals = sorted(pentagonals)
        return pentagonals
    