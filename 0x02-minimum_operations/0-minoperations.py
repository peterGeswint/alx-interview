#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n 'H' characters.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to get exactly n 'H' characters.
    
    :param n: The number of 'H' characters desired.
    :return: The minimum number of operations required.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2

    while n > 1:
        # If n is divisible by the current factor, apply it
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
