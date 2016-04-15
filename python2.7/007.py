"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def prob7(n):
    prime = 0
    for x in xrange(1, n + 1):
        prime = next_prime(prime)
    return prime


def next_prime(n):
    if n < 1:
        return 2

    next_ = n + 1 if n in (1, 2) else n + 2
    while not is_prime(next_):
        next_ += 2

    return next_


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0 or n < 2:
        return False

    for x in xrange(3, n, 2):
        if n % x == 0:
            return False
    return True


if __name__ == '__main__':
    print prob7(10001)
