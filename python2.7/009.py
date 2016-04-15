"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def prob9(triplet_sum):
	c_max = triplet_sum - 2
	c_min = 335

	for c in xrange(c_max, c_min, -1):
		for b in xrange(c - 1, 2, -1):
			for a in xrange(b - 1, 1, -1):
				if a + b + c < triplet_sum:
					break

				if a + b + c == triplet_sum and a**2 + b**2 == c**2:
					return a * b * c


if __name__ == '__main__':
    print prob9(1000)
