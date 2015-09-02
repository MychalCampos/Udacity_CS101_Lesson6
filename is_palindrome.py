# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:33:17 2015
# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?
@author: Mychal
"""


def is_palindrome(s):
    if s == '':  # base case
        return True
    else:
        if s[0] != s[-1]:
            return False
        else:
            return is_palindrome(s[1:-1])


print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True