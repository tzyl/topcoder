class AvoidRoads(object):
    def numWays(self, width, height, bad):
        A = [[0] * (width + 1) for _ in xrange(height + 1)]
        A[0][0] = 1
        # Fill boundaries.
        for i in xrange(1, height + 1):
            if self.blocked(i, 0, i - 1, 0, bad):
                break
            A[i][0] = 1
        for j in xrange(1, width + 1):
            if self.blocked(0, j, 0, j - 1, bad):
                break
            A[0][j] = 1
        # Fill in table using previous solved data.
        for i in xrange(1, height + 1):
            for j in xrange(1, width + 1):
                if not self.blocked(i, j, i - 1, j, bad):
                    A[i][j] += A[i - 1][j]
                if not self.blocked(i, j, i, j - 1, bad):
                    A[i][j] += A[i][j - 1]
        return A[height][width]

    def blocked(self, pt1_h, pt1_w, pt2_h, pt2_w, bad):
        return ("%s %s %s %s" % (pt1_w, pt1_h, pt2_w, pt2_h) in bad or
                "%s %s %s %s" % (pt2_w, pt2_h, pt1_w, pt1_h) in bad)

if __name__ == '__main__':
    print AvoidRoads().numWays(6, 6, ["0 0 0 1", "6 6 5 6"])
