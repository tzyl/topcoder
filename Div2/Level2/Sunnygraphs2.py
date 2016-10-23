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

# Hero's goal is to create a final graph in which the vertices 0 through
# n-1 are all in the same connected component. (I.e., there must be a way
# to reach any of these vertices from any other of them by following one
# or more consecutive edges, possibly visiting vertex n along the way.)
# Note that Hero does not care whether vertex n is in the same component
# as the other vertices: both possibilities are fine. In step 2 of the
# above procedure Hero has 2^n possible subsets to choose from. A choice
# of M is good if it produces a graph with the desired property. Count how
# many of the 2^n possibilities are good choices. Return that count as a
# long.


class Sunnygraphs2(object):
    def count(self, a):
        n = len(a)
        seen = set()
        cycle_lengths = []
        # Find all cycles in the original graph.
        for i in xrange(n):
            if i not in seen:
                j = i
                for _ in xrange(n):
                    j = a[j]
                    if j == i:
                        # Found a cycle let's mark the cycle as seen and calculate
                        # its length.
                        seen.add(i)
                        j = a[i]
                        cycle_length = 1
                        while j != i:
                            seen.add(j)
                            j = a[j]
                            cycle_length += 1
                        cycle_lengths.append(cycle_length)
                        break
        # m represents the number of vertices not in cycles.
        m = n - sum(cycle_lengths)
        # Now we can choose any subset of vertices not in cycles as long as we
        # choose at least one vertex from each cycle component.
        result = 1 << m
        for cycle_length in cycle_lengths:
            result *= (1 << cycle_length) - 1
        if len(cycle_lengths) == 1:
            # Only one cycle so one connected component, picking no vertices is
            # a valid choice.
            result += 1
        return result


if __name__ == '__main__':
    print Sunnygraphs2().count([29,34,40,17,16,12,0,40,20,35,5,13,27,7,29,13,14,39,42,9,30,38,27,40,34,33,42,20,29,42,12,29,30,21,4,5,7,25,24,17,39,32,9])
