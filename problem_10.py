"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def problem_10(n):
    primes = [2]
    attempt = 3
    result = 2

    while attempt < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
            result += attempt
        attempt += 2

    return result
