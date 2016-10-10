class Jewelry(object):
    def howMany(self, values):
        """Process elements group by group rather than element by element."""
        n = len(values)
        max_ = sum(values)
        values = list(values)
        values.sort()
        count = 0
        # Calculate groups.
        i = 0
        while i < n:
            # Calculate length of this group.
            G = 1
            while i + G < n and values[i + G] == values[i]:
                G += 1
            # ways_below[s] will be the number of ways to make sum s using
            # elements below element i.
            ways_below = [0] * (max_ + 1)
            ways_below[0] = 1
            for k in xrange(i):
                for s in xrange(max_, values[k] - 1, -1):
                    ways_below[s] += ways_below[s-values[k]]
            # g represents the nummber of elements in this group given to Bob.
            for g in xrange(1, G + 1):
                # ways_above[s] will be the number of ways to make sum s using
                # elements above element i + g - 1.
                ways_above = [0] * (max_ + 1)
                ways_above[0] = 1
                for k in xrange(i + g, n):
                    for s in xrange(max_, values[k] - 1, -1):
                        ways_above[s] += ways_above[s-values[k]]
                # Add contribution to count taking into account the number of
                # ways of choosing the g equal elements from G.
                for s in xrange(g * values[i], max_ + 1):
                    count += nCr(G, g) * ways_below[s-g*values[i]] * ways_above[s]
            i += G
        return count

    def howManyImproved(self, values):
        """Faster method of doing the same thing but still not taking into
        account equal value elements.
        """
        n = len(values)
        max_ = sum(values)
        values.sort()
        count = 0
        for i in xrange(n):
            # Element i of values is Bob's most expensive piece of jewelry.
            # ways_below[s] will be the number of ways to make sum s using
            # elements below element i.
            ways_below = [0] * (max_ + 1)
            ways_below[0] = 1
            for k in xrange(i):
                for s in xrange(max_, values[k] - 1, -1):
                    ways_below[s] += ways_below[s-values[k]]
            # ways_below[s] will be the number of ways to make sum s using
            # elements above element i.
            ways_above = [0] * (max_ + 1)
            ways_above[0] = 1
            for k in xrange(i + 1, n):
                for s in xrange(max_, values[k] - 1, -1):
                    ways_above[s] += ways_above[s-values[k]]
            for s in xrange(values[i], max_ + 1):
                count += ways_below[s-values[i]] * ways_above[s]
        return count

    def howManyInitial(self, values):
        """Sort values. Let A[i][j] be the number of ways with values[i] as the
        most expensive piece of jewelry given to Bob with each Frank and Bob
        receiving total value j of jewelry. Similary, let B[i][j] be the number
        of ways with values[i] as the least expensive piece of jewelry given to
        Frank with each receiving total value j of jewelry.

        Then number of ways will be the sum of A[i][k] * B[i][k], i < j, over
        possible total values k of jewelry given to each person.

        O(30*1000*n^2) where n is the number of pieces of jewelry (len(values).

        This solves the problem if all elements are distinct. The problem is if
        we have multiple elements with the same value as then it is not true
        that Bob's items are always to the left of Frank's items.
        """
        n = len(values)
        x = sum(values)
        values.sort()
        non_zero = set()
        # Populate A and B.
        A = [[0] * (x + 1) for _ in xrange(n)]
        B = [[0] * (x + 1) for _ in xrange(n)]
        for i in xrange(1, 2**n):
            lsb = get_lsb(i)
            msb = get_msb(i)
            total = int_to_total(i, values)
            A[msb][total] += 1
            B[lsb][total] += 1
            non_zero.add(total)
        # Calculate number of ways.
        ways = 0
        for k in non_zero:
            for i in xrange(n - 1):
                for j in xrange(i + 1, n):
                    ways += A[i][k] * B[j][k]
        return ways


def nCr(n, r):
    """Returns n choose r."""
    if r > n / 2:
        return nCr(n, n - r)
    if r == 0:
        return 1
    top = 1
    bottom = 1
    for i in xrange(r):
        top *= n - i
        bottom *= i + 1
    return top / bottom


def get_lsb(x):
    """Gets least significant 1 bit. Returns -1 if none."""
    if not x:
        return -1
    i = 0
    while not x & 1 << i:
        i += 1
    return i


def get_msb(x):
    """Gets most significant 1 bit. Returns -1 if none."""
    i = -1
    while x:
        x >>= 1
        i += 1
    return i


def int_to_total(x, values):
    """Returns the total value of jewelry represented by the subset of values
    given by the bits of x."""
    return sum(values[i] for i in xrange(len(values)) if x & 1 << i)

if __name__ == '__main__':
    print Jewelry().howMany([7, 7, 8, 9, 10, 11, 1, 2, 2, 3, 4, 5, 6])
    print Jewelry().howMany([1, 2, 3, 4, 5])
    print Jewelry().howMany([1, 2, 5, 3, 4, 5])
    print Jewelry().howMany([1000] * 30)
    # print Jewelry().howMany2([7, 7, 8, 9, 10, 11, 1, 2, 2, 3, 4, 5, 6])
    # print Jewelry().howMany2([1, 2, 3, 4, 5])
    # print Jewelry().howMany2([1, 2, 5, 3, 4, 5])
    # print Jewelry().howMany2([1000] * 19)
