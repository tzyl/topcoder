# You have implemented a sorting algorithm that requires exactly c*n*lg(n)
# nanoseconds to sort n integers. Here lg denotes the base-2 logarithm.
# Given time nanoseconds, return the largest double n such that c*n*lg(n)
# <= time.
from math import log


class SortEstimate(object):
    def howMany(self, c, time):
        n = 0
        increment = 1000000000
        while increment >= 1e-9:
            x = n + increment
            if c * x * log(x, 2) <= time:
                n += increment
            increment /= 2.0
        return n


if __name__ == '__main__':
    print SortEstimate().howMany(1, 2000000000)
