class WalkOverATree(object):
    def maxNodesVisited2(self, parent, L):
        # Take advantage of the point: For each i, parent[i] will be between
        # 0 and i, inclusive.
        n = len(parent) + 1
        distances = [0] * n
        max_distance = 0
        for i, p in enumerate(parent, 1):
            distances[i] = distances[p] + 1
            max_distance = max(max_distance, distances[i])
        max_distance = min(max_distance, L)
        return min(n, 1 + max_distance + (L - max_distance) / 2)

    def maxNodesVisited2(self, parent, L):
        # First group the nodes by children of each parent.
        n = len(parent) + 1
        children = [[] for _ in xrange(n)]
        for i, p in enumerate(parent, 1):
            children[p].append(i)
        # Now use BFS to find furthest distance from root.
        boundary = [0]
        distance = -1
        while boundary:
            distance += 1
            next_boundary = []
            for node in boundary:
                for child in children[node]:
                    next_boundary.append(child)
            boundary = next_boundary
        return min(1 + L, n, 1 + distance + (L - distance) / 2)
