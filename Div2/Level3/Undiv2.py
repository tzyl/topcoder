# Given a positive integer x, let s(x) be the second smallest positive
# integer that does not divide x.

# For example, let x = 6. The integers that do not divide x are 4, 5, 7,
# 8, 9, 10, ... The second smallest of these is 5. Hence we have s(6) = 5.

# Hero took a blank sheet of paper. For each i between 1 and n, inclusive,
# he computed the value s(i) and wrote it on the paper. You are given the
# n. Compute and return the sum of the n numbers on Hero's paper.


class Undiv2(object):
    def getsum(self, n):
        # The smallest number not dividing x <= 1e9 can be no larger than 23
        # otherwise lcm(1,...,23) > x. Hence the second largest number not
        # divinding x can be no larger than 46.
        total = 0
        for i in xrange(1, 47):
            for j in xrange(1, i):
                # Count how many numbers x <= 1e9 have smallest number not
                # divinding j and second smallest i. This must mean that x is
                # a multiple of 1,...,j-1,j+1,...,i-1.
                m = lcm_list(range(1, j) + range(j + 1, i))
                # Count how many numbers are multiples of these factors but not
                # multiples of i and j (using inclusion exclusion).
                count = n / m - n / lcm(m, i) - n / lcm(m, j) + n / lcm_list([m, i, j])
                # Add the contribution of count to the total.
                total += i * count
        return total


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def lcm_list(A):
    result = 1
    for num in A:
        result = lcm(result, num)
    return result


if __name__ == '__main__':
    print Undiv2().getsum(3)
