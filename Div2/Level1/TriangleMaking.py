class TriangleMaking(object):
    def maxPerimeter(self, a, b, c):
        sides = [a, b, c]
        sides.sort()
        return min(sum(sides), 2 * (sides[0] + sides[1]) - 1)
