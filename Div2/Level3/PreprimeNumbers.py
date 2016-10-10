class PreprimeNumbers(object):
    # Too much memory for TopCoder limits using Python.
    def nthNumber(self, n):
        max_limit = 6000000
        # exponent_sums[x] is the sum of the exponents in the prime
        # factorization of x. If x has only one prime factor we decrease this
        # sum by one so that x is preprime iff exponent_sums[x] = 2.
        # In this system exponent_sums[x] == 0 iff x is prime
        exponent_sums = [0] * max_limit
        x = 2
        count = 0
        while count < n:
            if exponent_sums[x] == 0:
                # x is prime. Increment the exponent count of all of its
                # multiples.
                for y in xrange(2 * x, max_limit, x):
                    z = y
                    while z % x == 0:
                        exponent_sums[y] += 1
                        z /= x
                    if z == 1:
                        # y must be an exact power of x so we need to decrement
                        # its exponent sum by one.
                        exponent_sums[y] -= 1
            elif exponent_sums[x] == 2:
                count += 1
            x += 1
        return x - 1


if __name__ == '__main__':
    print PreprimeNumbers().nthNumber(1000000)
