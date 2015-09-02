# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:18:06 2015
# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.
@author: Mychal
"""


def factorial(n):
    if n == 0:  # base case (or terminating case)
        return 1
    else:
        # not circular logic as we have a terminating case above
        # i.e., code keeps going until we hit n = 0        
        return n * factorial(n-1)


print factorial(0)
#>>> 1

print factorial(5)
#>>> 120

print factorial(10)
#>>> 3628800