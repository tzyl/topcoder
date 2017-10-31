# A tournament is a directed graph on n vertices that can be obtained by
# taking an undirected complete graph on n vertices and assigning a
# direction to each edge. The outdegree of a vertex is the number of
# directed edges that start at that vertex. The score of a tournament is
# the list of the outdegrees of its vertices, in no particular order.

# Alice used to have a tournament T but she lost it. She only remembers
# its score. You are given the score of T in the s.

# Determine and return the number of pairs of vertices (u,v) such that in
# the tournament T the vertex v was reachable from the vertex u. Note that
# each vertex is reachable from itself.

# You may assume that the answer can always be uniquely determined.

# - s will contain between 1 and 100 elements, inclusive.
# - s will be a valid score of some tournament.


class ScoresSequence:
    def count(self, s):
        count = 0
        tournament = self.construct_tournament(s)
        # 2-partition-transitive tournament
        # Sorted s_1 >= s_2 >= ... >= s_n.
        # i beats j whenever i < j and i = j mod 2.
        s = list(s)
        s.sort()
        S1 = []
        S2 = []
        # Split into S1, S2.
        for i, out_degree in enumerate(s):
            if i % 2 == 0:
                S1.append(out_degree - (i // 2))
            else:
                S2.append(out_degree - (i // 2))
            count += i // 2
        S1.sort()
        S2.sort()


    def construct_tournament(self, s):
        # n vertices 0, ..., n - 1.
        A = []
        for i in range(n):
            for j in range(n):
                pass
