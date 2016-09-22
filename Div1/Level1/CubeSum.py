class CubeSum(object):
    def count(self, N):
        return self.count_helper(N)

    def count_helper(self, N, i=0, max_=float("inf")):
        if N == 0:
            return 1
        if i == 3:
            root = int(round(N ** (1.0 / 3)))
            if root ** 3 == N and root <= max_:
                return 1
            else:
                return 0
        total = 0
        x = int(round((N / 4.0) ** (1.0 / 3)))
        while x ** 3 <= N and x <= max_:
            total += self.count_helper(N - x ** 3, i + 1, x)
            x += 1
        return total

if __name__ == '__main__':
    print CubeSum().count(100000000)
