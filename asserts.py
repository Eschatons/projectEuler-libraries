# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:15:58 2016

@author: efron
"""

"""asserts.py contains a number of assertions to make typing a little stronger.
"""
import numbers
import decimal
def real_number(*args):
    for arg in args:
        if not isinstance(arg, numbers.Real):
            raise(TypeError('arg is not a real number'))
    
def integer(*args):
    for arg in args:
        if not isinstance(arg, numbers.Integral):
            raise(TypeError('arg is not an integer number'))

def numeric(*args):
    for arg in args:
        dec = isinstance(arg, decimal.Decimal)
        number = isinstance(arg, numbers.Number)
        if not dec or number:
            raise(TypeError('arg is not a python number or decimal'))

def string(*args):
    for arg in args:
        if not isinstance(arg, str):
            raise(TypeError('arg is not a string'))