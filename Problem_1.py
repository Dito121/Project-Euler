"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np


def sum_of_3_5_multiples(N):
    numbers = np.arange(1, N)
    summ = 0

    for i in range(len(numbers)):
        if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
            summ += numbers[i]
        elif numbers[i] % 3 == 0:
            summ += numbers[i]
        elif numbers[i] % 5 == 0:
            summ += numbers[i]

    return summ
