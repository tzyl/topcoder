class BadNeighbors(object):
    def maxDonations(self, donations):
        return max(self.maxDonationsRange(donations[:-1]), self.maxDonationsRange(donations[1:]))

    def maxDonationsRange(self, donations):
        best = []
        for i, donation in enumerate(donations):
            best.append(donation)
            for j in xrange(i - 1):
                if best[j] + donation > best[i]:
                    best[i] = best[j] + donation
        return max(best)

print BadNeighbors().maxDonations([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72])
