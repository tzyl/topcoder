#  Problem Statement for grafixMask


# Problem Statement

# Note: This problem statement includes images that may not appear if you
# are using a plugin. For best results, use the Arena editor.

# In one mode of the grafix software package, the user blocks off portions
# of a masking layer using opaque rectangles. The bitmap used as the
# masking layer is 400 pixels tall and 600 pixels wide. Once the
# rectangles have been blocked off, the user can perform painting actions
# through the remaining areas of the masking layer, known as holes. To be
# precise, each hole is a maximal collection of contiguous pixels that are
# not covered by any of the opaque rectangles. Two pixels are contiguous
# if they share an edge, and contiguity is transitive.

# You are given a String[] named rectangles, the elements of which specify
# the rectangles that have been blocked off in the masking layer. Each
# String in rectangles consists of four integers separated by single
# spaces, with no additional spaces in the string. The first two integers
# are the window coordinates of the top left pixel in the given rectangle,
# and the last two integers are the window coordinates of its bottom right
# pixel. The window coordinates of a pixel are a pair of integers
# specifying the row number and column number of the pixel, in that order.
# Rows are numbered from top to bottom, starting with 0 and ending with
# 399. Columns are numbered from left to right, starting with 0 and ending
# with 599. Every pixel within and along the border of the rectangle
# defined by these opposing corners is blocked off.

# Return a int[] containing the area, in pixels, of every hole in the
# resulting masking area, sorted from smallest area to greatest.


# Definition

# Class:  grafixMask
# Method: sortedAreas
# Parameters: String[]
# Returns:    int[]
# Method signature:   int[] sortedAreas(String[] rectangles)
# (be sure your method is public)


# Notes
# -   Window coordinates are not the same as Cartesian coordinates. Follow the definition given in the second paragraph of the problem statement.

# Constraints
# -   rectangles contains between 1 and 50 elements, inclusive
# -   each element of rectangles has the form "ROW COL ROW COL", where: "ROW" is a placeholder for a non-zero-padded integer between 0 and 399, inclusive; "COL" is a placeholder for a non-zero-padded integer between 0 and 599, inclusive; the first row number is no greater than the second row number; the first column number is no greater than the second column number
from collections import deque


class grafixMask(object):
    def sortedAreas(self, rectangles):
        bitmap = [[0] * 600 for _ in xrange(400)]
        areas = []
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        # Block off rectangles as 1s.
        bitmap = self.block_rectangles(bitmap, rectangles)
        # Run BFS from each unfilled hole to calculate areas.
        for unfilled in self.find_unfilled(bitmap):
            area = 0
            queue = deque([unfilled])
            bitmap[unfilled[0]][unfilled[1]] = 1
            while queue:
                i, j = queue.popleft()
                area += 1
                for x, y in zip(dx, dy):
                    if 0 <= i + y < len(bitmap) and 0 <= j + x < len(bitmap[0]):
                        if bitmap[i + y][j + x] == 0:
                            queue.append((i + y, j + x))
                            bitmap[i + y][j + x] = 1
            areas.append(area)
        areas.sort()
        return areas

    def block_rectangles(self, bitmap, rectangles):
        for rectangle in rectangles:
            i1, j1, i2, j2 = map(int, rectangle.split())
            for i in xrange(i1, i2 + 1):
                for j in xrange(j1, j2 + 1):
                    bitmap[i][j] = 1
        return bitmap

    def find_unfilled(self, bitmap):
        for i in xrange(len(bitmap)):
            for j in xrange(len(bitmap[0])):
                if bitmap[i][j] == 0:
                    yield i, j

if __name__ == '__main__':
    print grafixMask().sortedAreas(["0 292 399 307"])
    print grafixMask().sortedAreas(["48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"])
    print grafixMask().sortedAreas(["0 192 399 207", "0 392 399 407", "120 0 135 599", "260 0 275 599"])
    print grafixMask().sortedAreas(["50 300 199 300", "201 300 350 300", "200 50 200 299", "200 301 200 550"])
    print grafixMask().sortedAreas(["0 20 399 20", "0 44 399 44", "0 68 399 68", "0 92 399 92", "0 116 399 116", "0 140 399 140", "0 164 399 164", "0 188 399 188", "0 212 399 212", "0 236 399 236", "0 260 399 260", "0 284 399 284", "0 308 399 308", "0 332 399 332", "0 356 399 356", "0 380 399 380", "0 404 399 404", "0 428 399 428", "0 452 399 452", "0 476 399 476", "0 500 399 500", "0 524 399 524", "0 548 399 548", "0 572 399 572", "0 596 399 596", "5 0 5 599", "21 0 21 599", "37 0 37 599", "53 0 53 599", "69 0 69 599", "85 0 85 599", "101 0 101 599", "117 0 117 599", "133 0 133 599", "149 0 149 599", "165 0 165 599", "181 0 181 599", "197 0 197 599", "213 0 213 599", "229 0 229 599", "245 0 245 599", "261 0 261 599", "277 0 277 599", "293 0 293 599", "309 0 309 599", "325 0 325 599", "341 0 341 599", "357 0 357 599", "373 0 373 599", "389 0 389 599"])
