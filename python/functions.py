#!/usr/bin/env python3

# This is required if you want to run this python 3 program in python 2:
#from __future__ import division

# Function with two arguments, one that has a default value
def get_at_content(seq, significant_digits=2):
    val = (seq.count('A') + seq.count('T')) / len(seq)
    return round(val, significant_digits)  # round

# Some tests:
assert(get_at_content("A") == 1)
assert(get_at_content("ATGC") == 0.5)

seq = "AATGGCGTTATGGTAAAG"
print(str(get_at_content(seq)))

# You can invoke a function with keyword arguments:
print(str(get_at_content(seq=seq, significant_digits=4)))
