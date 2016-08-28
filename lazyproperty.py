# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:14:01 2016

@author: efron
"""

class LazyProperty:
    '''a decorator that lazily computes the property given by function func, 
    memoizing for further use. Usage taken from Python Cookbook by
    David Beaszley and Brian K Jones
    
    example:
        from math import sqrt          
        class Vector:
        def __init__(self, *args):
            self._items = tuple(x for x in args)
            self._len = len(self._items)
        
        def __getitem__(self, index):
            return self._items[index]
            
        def __len__(self):
            return self._len
        
        def __
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
            
        In [58]: W = Vector(1, 3, 5)

    In [59]: W.mean
    computing mean
    Out[59]: 3.0

    In [60]: W.variance
    computing variance
    Out[60]: 2.6666666666666665

    In [61]: W.standardDeviation
    computing standard deviation
    Out[61]: 1.632993161855452

    In [62]: V = Vector(2, 8, -5, 12)

    In [63]: V.standardDeviation
    computing standard deviation
    computing variance
    computing mean
    Out[63]: 6.417748826496718
'''
    
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
from math import sqrt          
