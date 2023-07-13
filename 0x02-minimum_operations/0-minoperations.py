#!/usr/bin/python3

''' A module that returns the minimum Operations'''

def minOperations(n):
     '''returns the minimum operations to get n H's'''
     if (n < 2):
        return 0
    operations, root = 0, 2
    while root <= n:
        # if n evenly divides by root means no remainder
        if n % root == 0:
            # total even-divisions by root = total operations
            operations += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return operations
