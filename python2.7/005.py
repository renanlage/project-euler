"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


def is_divisible(n):
    return n % 20 == 0 and n % 18 == 0 and n % 16 == 0 and n % 12 == 0


def problem5():
    primes = (19, 17, 13, 11, 7, 5, 3, 3, 2, 2, 2, 2)
    return reduce(lambda x, y: x * y, primes)


if __name__ == '__main__':
    print problem5()


