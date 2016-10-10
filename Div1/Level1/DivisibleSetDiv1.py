class DivisibleSetDiv1(object):
    def isPossible(self, b):
        # b[0],...,b[n-1] between 1 and 10. 2 <= n <= 50.
        # a[i] > 1 distinct.
        # a[i] ^ b[i] divisible by p[i] = a[0]*...*a[i-1]*a[i+1]*...*a[n-1].
        # We must have all a[i] must be divisible by some prime.
        # Let x be the sum of all the exponents of y in the a[i].
        # Then we need lg_y(a[i]) * b[i] >= x - lg_y(a[i])
        # Hence lg_y(a[i]) * (b[i] + 1) >= x.
        # By summing over all i we then have sum_i(1 / (b[i] + 1)) <= 1.
        x = 1
        for num in b:
            x *= (num + 1)
        test = sum(x / (num + 1) for num in b)
        if test > x:
            return "Impossible"
        elif len(set(b)) != len(b):
            # The elements of b are non-distinct.
            return "Impossible" if test == x else "Possible"
        return "Possible"

if __name__ == '__main__':
    print DivisibleSetDiv1().isPossible([7, 7, 7])
