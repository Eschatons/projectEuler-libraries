# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:44:18 2016

@author: efron
"""

from combinatorics import PartitionCount




def test_fill_partition():
    filled = PartitionCount(500, fillPartitionTree = True)
    manually_filled = PartitionCount(500, fillPartitionTree = False)
    for n in range(2, 500):
        manually_filled.count_partitions(n)
    for n in range(500):
        assert(filled[n] == manually_filled[n], 'filling manually does not work!')
    print('test succeeded!')

test_fill_partition()