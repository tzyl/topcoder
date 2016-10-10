class CityLink(object):
    def timeTaken(self, x, y):
        # Quicker solution.
        n = len(x)
        cities = zip(x, y)
        distances = [[0] * n for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(n):
                dx = abs(cities[i][0] - cities[j][0])
                dy = abs(cities[i][1] - cities[j][1])
                if dx == 0:
                    distances[i][j] = (dy + 1) / 2
                elif dy == 0:
                    distances[i][j] = (dx + 1) / 2
                else:
                    distances[i][j] = max(dx, dy)
        # Floyd-Warshall algorithm.
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    distances[i][j] = min(distances[i][j], max(distances[i][k], distances[k][j]))
        return max(distances[i][j] for i in xrange(n) for j in xrange(n))

    def timeTaken2(self, x, y):
        # Work out distance between all pairs of citites.
        # Define distance here as the minimum amount of time it takes
        # to directly connect the two cities with a road.
        n = len(x)
        if n == 1:
            return 0
        cities = zip(x, y)
        distances = []
        for i in xrange(n - 1):
            for j in xrange(i + 1, n):
                dx = abs(cities[i][0] - cities[j][0])
                dy = abs(cities[i][1] - cities[j][1])
                if dx == 0:
                    distance = (dy + 1) / 2
                elif dy == 0:
                    distance = (dx + 1) / 2
                else:
                    distance = max(dx, dy)
                distances.append((distance, i, j))
        distances.sort(key=lambda x: x[0])
        print distances
        connected = [set([i]) for i in xrange(n)]
        m = 0
        while len(connected) > 1:
            a = distances[m][1]
            b = distances[m][2]
            for i, component in enumerate(connected):
                if a in component:
                    c1 = i
                if b in component:
                    c2 = i
            if c1 != c2:
                connected[c1] = connected[c1].union(connected[c2])
                del connected[c2]
            m += 1
        return distances[m - 1][0]

if __name__ == '__main__':
    print CityLink().timeTaken([0, 0], [30, -59])
    print CityLink().timeTaken([1593,-88517,14301,3200,6,-15099,3200,5881,-2593,11,57361,-92990], [99531,-17742,-36499,1582,46,34001,-19234,1883,36001,0,233,485])
