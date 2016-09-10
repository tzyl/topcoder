class EvenRoute(object):
    def isItPossible(self, x, y, wantedParity):
        possible = False
        for i in xrange(len(x) - 1):
            for j in xrange(i + 1, len(x)):
                if (y[j] - y[i] + x[j] - x[i]) % 2 == 1:
                    return "CAN"
        # All edges between nodes other than (0, 0) must be even.
        # Check whether we have a starting edge with the correct parity.
        for i in xrange(len(x)):
            if (x[i] + y[i]) % 2 == wantedParity:
                possible = True
        return "CAN" if possible else "CANNOT"

print EvenRoute().isItPossible([11, 21, 0], [-20, 42, 7], 0)
