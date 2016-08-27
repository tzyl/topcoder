class LastStone(object):
    def numWins(self, turns, m, n):
        wins = [False] * 100001
        for start in xrange(1, 100001):
            if any(not wins[start - move] for move in turns if start - move >= 0):
                wins[start] = True
        return sum(wins[start] for start in xrange(m, n + 1))

# print LastStone().numWins([1, 3, 5, 32, 56, 77, 89, 91, 93], 1, 100000)
