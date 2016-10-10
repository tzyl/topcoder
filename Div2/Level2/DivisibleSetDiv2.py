class DivisibleSetDiv2(object):
    def isPossible(self, b):
        # b[0],...,b[n-1] between 1 and 10. 1 <= n <= 50.
        # Let a[i] = 2^x[i]. Then we need b[i]*x[i] >= y where y = sum(x) for
        # all i. Hence x[i] >= y / b[i] and summing over i we get
        # sum(1/b[i]) <= 1.
        n = len(b)
        if n == 1:
            return "Possible"
        elif n > 10:
            return "Impossible"
        x = 1
        for num in b:
            x *= num
        return "Possible" if sum(x / num for num in b) <= x else "Impossible"

if __name__ == '__main__':
    print DivisibleSetDiv2().isPossible([3, 2])
