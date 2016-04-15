"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    str_n = str(n)
    for i in xrange(len(str_n) / 2):
        if str_n[i] != str_n[-i - 1]:
            return False
    return True


def prob4():
    max_ = 0
    for n1 in xrange(999, 99, -1):
        for n2 in xrange(n1, 99, -1):
            prod = n1 * n2

            if max_ >= n1 * n1:
                return max_

            if max_ >= prod:
                break

            if is_palindrome(prod):
                max_ = prod

    return max_


if __name__ == '__main__':
    print prob4()
