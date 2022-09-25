"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import numpy as np


def problem_5(n):
    factors = np.arange(2, n+1)
    smallest = False
    test = 10

    while not smallest:
        test += 1
        for factor in factors:
            if test % factor != 0:
                break
        else:
            smallest = True

    return test
