class FactorialGCD(object):
    def factGCD(self, a, b):
        if a == 0:
            return 1
        result = 1
        # First work out the prime factors of b.
        for i in xrange(2, int(b ** (1.0 / 2)) + 1):
            b_count = 0
            while b % i == 0:
                b_count += 1
                b /= i
            if b_count:
                # Find how many times i divides into a!.
                a_count = 0
                for j in xrange(i, a + 1, i):
                    if a_count >= b_count:
                        break
                    while j % i == 0 and a_count < b_count:
                        a_count += 1
                        j /= i
                result *= i ** min(a_count, b_count)
        # Check if b is prime and if it will divide a! (a >= b).
        if b != 1 and a >= b:
            result *= b
        return result


if __name__ == '__main__':
    # print FactorialGCD().factGCD(5, 20)
    print FactorialGCD().factGCD(7, 5040)
