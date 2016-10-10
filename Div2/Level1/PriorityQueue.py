class PriorityQueue(object):
    def findAnnoyance(S, a):
        N = len(a)
        annoyance = 0
        for i in reversed(xrange(N)):
            if S[i] == "b":
                for j in xrange(i):
                    annoyance += a[j]
        return annoyance
