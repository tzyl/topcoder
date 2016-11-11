class GerrymanderEasy(object):
    def getmax(self, A, B, K):
        best = 0
        n = len(A)
        # i will be the starting vertex.
        for i in xrange(n - K + 1):
            a, b = 0, 0
            # Add the first K - 1 districts.
            for j in xrange(K - 1):
                a += A[i + j]
                b += B[i + j]
            # For each of the remaining districs add them one by one and keep
            # track of the best ratio with i as the starting district.
            for j in xrange(K - 1, n - i):
                a += A[i + j]
                b += B[i + j]
                current = float(b) / a
                best = max(best, current)
        return best


if __name__ == '__main__':
    print GerrymanderEasy().getmax([5, 1, 2, 7], [4, 0, 2, 2], 2)
    print GerrymanderEasy().getmax([1] * 1000, [0] * 1000, 2)
    print GerrymanderEasy().getmax(range(1, 1001), [max(0, x - 1) for x in range(1, 1001)], 6)
