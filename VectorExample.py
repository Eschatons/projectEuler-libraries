# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 13:19:43 2016

@author: efron
"""
from lazyproperty import LazyProperty
from math import sqrt
from itertools import chain

class Vector:
    ''' example class to play around with python magic'''
    def __init__(self, *args):
        self._items = tuple(x for x in chain(args))
        self._len = len(self._items)
        self._operationError = TypeError('''arithmetic operation only
        defined for vectors of same length or scalars''')
        
    def __getitem__(self, index):
        return self._items[index]
        
    def __len__(self):
        return self._len
        
    def __abs__(self):
        return self._abs
        
    def __bool__(self):
        return abs(self) > 0
        
    def __str__(self):
        return str(self[:])
    
    def __repr__(self):
        return 'Vector{0}'.format(str(self))
        
    def __neg__(self):
        return Vector(-k for k in self)
    def __add__(self, other):
        if  len(self) == len(other):
            return Vector(tuple(self[i] + other[i] for i in range(len(self))))
        else:
            raise self.opertionError
    def __sub__(self, other):
        if  len(self) == len(other):
            return Vector(tuple(self[i] - other[i] for i in range(len(self))))
        else:
            raise(self._operationError)
    def __mul__(self, other):
        if  len(self) == len(other):
            return Vector(self[i] * other[i] for i in range(len(self)))
        else:
            raise(self._operationError)
    
    def __div__(self, other):
        if  len(self) == len(other):
            return Vector(self[i] / other[i] for i in range(len(self)))
        else:
            raise(self._operationError)
        
    def __matmul__(self, other):
        if  len(self) == len(other):
            return sum((self[i]*other[i]) for i in range(len(self)))
        
    def __radd__(self, other):
        return self + other
    def __rsub__(self, other):
        return self - other
    def __rmul__(self, other):
        return self * other
    def __rdiv__(self, other):
        return self / other
    def __rmatmul__(self, other):
        return self @ other
    
    # lazy properties
    
    @LazyProperty
    
    def _abs(self):
        print('computing abs')
        return sqrt(sum(x**2 for x in self))
    @LazyProperty
    def mean(self):
        print('computing mean')
        return sum(k for k in self) / len(self)
    @LazyProperty
    def variance(self):
        print('computing variance')
        return (sum((self.mean - k)**2 for k in self)) / len(self)
        
    @LazyProperty
    def standardDeviation(self):
        print('computing standard deviation')
        return sqrt(self.variance)