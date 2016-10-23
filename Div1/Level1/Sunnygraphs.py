# Hero has just constructed a very specific graph. He started with n
# isolated vertices, labeled 0 through n-1. For each vertex i Hero then
# chose a vertex a[i] (other than i) and he added an edge that connected i
# and a[i]. This way he created a graph with n vertices and n edges. Note
# that if a[x]=y and a[y]=x, the vertices x and y were connected by two
# different edges. Hero now wants to perform the following procedure:

# 1. Add a new isolated vertex number n.
# 2. Choose a subset M of the original vertices.
# 3. For each x in M, erase an edge between vertices x and a[x].
# 4. For each x in M, add a new edge between vertices x and n.

# Hero's goal is to create a final graph in which the vertices 0 and 1 are
# in the same connected component. (I.e., there is a path from one of them
# to the other.) In step 2 of the above procedure Hero has 2^n possible
# subsets to choose from. A choice of M is good if it produces a graph
# with the desired property. Count how many of the 2^n possibilities are
# good choices. Return that count as a long.


class Sunnygraphs(object):
    def count(self, a):
        n = len(a)
        # Classify vertices depending on whether they are:
        # - Reachable from both 0 and 1 (directed paths).
        # - Reachable by only one of 0 and 1.
        # - Not reachable by either of 0 or 1.
        i = 0
        reachable_zero = [False] * n
        while not reachable_zero[i]:
            reachable_zero[i] = True
            i = a[i]
        i = 1
        reachable_one = [False] * n
        while not reachable_one[i]:
            reachable_one[i] = True
            i = a[i]
        both = 0
        only_zero = 0
        only_one = 0
        neither = 0
        for i in xrange(n):
            if reachable_zero[i] and reachable_one[i]:
                both += 1
            elif reachable_zero[i]:
                only_zero += 1
            elif reachable_one[i]:
                only_one += 1
            else:
                neither += 1
        count = 0
        # If we pick at least one vertex from both then 0 and 1 are both
        # connected to n so they are in the same component. We are then free
        # to include or not include any of the n - both remaining vertices.
        count += ((2 ** both) - 1) * (2 ** (n - both))
        # We can also connect 0 and 1 to n by picking at least one vertex from
        # only_zero and at least one vertex from only_one. The vertices which
        # are neither connected to 0 or 1 can be included or not freely.
        count += ((2 ** only_zero) - 1) * ((2 ** only_one) - 1) * (2 ** neither)
        # If both > 0 then 0 and 1 are initially connected so we can leave the
        # connected vertices alone and choose those which are connected to
        # neither.
        if both:
            count += 2 ** neither
        return count


if __name__ == '__main__':
    print Sunnygraphs().count([18, 18, 20, 28, 7, 27, 8, 13, 40, 3, 7, 21, 30, 17, 13, 34, 29, 16, 15, 11, 0, 9, 39, 36, 38, 23, 24, 8, 4, 9, 29, 22, 35, 5, 13, 23, 3, 27, 34, 23, 8]) # 2198754820096
