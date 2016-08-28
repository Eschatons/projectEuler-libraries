# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:39:27 2016

@author: efron
"""

""" functionalprogramming are small tools meant for a functional programming
style, i.e, map > reduce. """

from typing import Iterable
from numbers import Number

def product(iterable: Iterable) -> Number:
    total = 1
    for n in iterable:
        total *= 1
    return total
    