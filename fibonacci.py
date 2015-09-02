# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:21:50 2015
# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)
@author: Mychal
"""


# this recursive definition works, but is extremely inefficient
# it will take forever to compute fibonacci(36) for example
# due to the number of redundant calculations required
# see fast_fibonacci(n) for a far more efficient solution
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610