"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def problem3(n, prime=2):
    while n % prime == 0:
        n /= prime

    if n == 1:
        return prime

    return problem3(n, next_prime(prime))


def next_prime(n):
    if n == 1:
        return 2

    next_ = n + 1 if n in (1, 2) else n + 2
    while not is_prime(next_):
        next_ += 2

    return next_


def is_prime(n):
    if n == 1 or n == 2:
        return True

    if n % 2 == 0:
        return False

    for x in xrange(3, n, 2):
        if n % x == 0:
            return False
    return True


if __name__ == '__main__':
    print problem3(600851475143)
