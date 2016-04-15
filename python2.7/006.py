"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def mod(n):
    return n if n >= 0 else -n


def problem6(n):
    pa_sum = (n + 1) * n / 2
    return mod(sum(x ** 2 for x in xrange(1, n + 1)) - pa_sum ** 2)


if __name__ == '__main__':
    print problem6(100)
