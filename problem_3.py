"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def find_prime_factors(N):
    factors = []
    for i in range(2, N // 2):
        if N % i == 0:
            factors.append(i)

    primes = []
    for factor in factors:
        for j in range(2, factor):
            if factor % j == 0:
                primes.append(j)

    result = []
    for factor in factors:
        if factor in primes:
            result.append(factor)

    return result


# find_prime_factors(600851475143)
