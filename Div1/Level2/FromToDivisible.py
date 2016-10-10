from collections import deque


class FromToDivisible(object):
    # O(M^2)
    def shortest(self, N, S, T, a, b):
        # BFS on b[0],...,b[M-1].
        M = len(a)
        d = [None] * M
        Q = deque()
        for i in xrange(M):
            if S % a[i] == 0:
                d[i] = 1
                Q.append(i)
        while Q:
            i = Q.popleft()
            if T % b[i] == 0:
                return d[i]
            for j in xrange(M):
                if d[j] is None and lcm(a[j], b[i]) <= N:
                    d[j] = d[i] + 1
                    Q.append(j)
        return -1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)
