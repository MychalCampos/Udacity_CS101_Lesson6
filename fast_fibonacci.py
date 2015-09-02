# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:03:31 2015
#Define a faster fibonacci procedure that will enable us to compute
#fibonacci(36).
@author: Mychal
"""


# # your solution
#def fast_fibonacci(n):
#    ls = [0,1]
#    if n <= 1:
#        return ls[n]
#    i = 2
#    while i <= n:
#        ls.append(ls[i-1] + ls[i-2])
#        i = i + 1
#    return ls[n]


# instructor's solution is more elegant and more efficient
# uses multiple assignment and keeps track of previous 
# 2 entries in a more clever way
def fast_fibonacci(n):
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after, current + after
    return current

print fast_fibonacci(36)
#>>> 14930352