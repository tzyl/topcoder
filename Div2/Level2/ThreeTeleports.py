# You are a frog. You live on an infinite lattice of grid points. For each
# pair of integers x, y there is a grid point with coordinates (x,y). At
# this moment, you sit on the grid point (xMe,yMe). You want to get home:
# to the grid point (xHome,yHome).

# There are two ways in which you can travel. Your first option is
# jumping: if you are at (x,y), you can jump to one of the four
# neighboring grid points: (x+1,y), (x-1,y), (x,y+1), or (x,y-1). Each
# jump takes one second.

# Your second option is using a teleport. There are three teleports in the
# entire world. Each of them connects two different grid points. If you
# are at one of the endpoints, you may activate the teleport and travel to
# its other endpoint. Traveling by teleport takes 10 seconds.

# You are given s xMe, yMe, xHome, yHome, and a teleports that describes
# the three teleports. Each element of teleports will be a containing four
# integers x1, y1, x2, and y2, separated by single spaces. These integers
# describe a teleport with endpoints at (x1,y1) and (x2,y2).

# Your method must return the shortest time in which you can reach your home.


class ThreeTeleports(object):
    def shortestDistance(self, xMe, yMe, xHome, yHome, teleports):
        # Dijkstra's algorithm.
        start = Node(xMe, yMe)
        end = Node(xHome, yHome)
        teleport_starts = [Node(*map(int, s.split())[:2]) for s in teleports]
        teleport_ends = [Node(*map(int, s.split())[-2:]) for s in teleports]
        Q = [start, end] + teleport_starts + teleport_ends
        start.d = 0
        while Q:
            current = min(Q, key=lambda x: x.d)
            Q.remove(current)
            for other in Q:
                if current.d + calculate_edge_weight(current, other, teleports) < other.d:
                    other.d = current.d + calculate_edge_weight(current, other, teleports)
                    other.p = current
        return end.d


class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = float("inf")
        self.p = None


def calculate_edge_weight(node1, node2, teleports):
    if ("%d %d %d %d" % (node1.x, node1.y, node2.x, node2.y) in teleports or
            "%d %d %d %d" % (node2.x, node2.y, node1.x, node1.y) in teleports):
        return 10
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)


if __name__ == '__main__':
    print ThreeTeleports().shortestDistance(3, 7, 10000, 30000, ["3 10 5200 4900", "12212 8699 9999 30011", "12200 8701 5203 4845"])
