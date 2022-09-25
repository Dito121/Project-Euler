"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import numpy as np


def problem_6(n):
    numbers = np.arange(1, n+1)
    sum_squares = numbers**2
    sum_squares = sum_squares.sum()

    square_sum = numbers.sum()
    square_sum = square_sum**2

    return square_sum - sum_squares
