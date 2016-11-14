# According to research conducted recently, listening to classical music
# increases one's mental abilities, while listening to metal decreases
# them. Now, yet another experiment is being conducted to try to prove or
# disprove this statement.

# In this new experiment, a mouse is placed in a rectangular maze
# consisting of NxM squares. Each square either contains a wall or is
# empty. The maze is structured in such a way that for any two empty
# squares, there exists exactly one path between them. A path is a
# sequence of pairwise distinct empty squares such that every two
# consecutive squares are neighboring. Two squares are considered
# neighboring if they share a common edge.

# One of the empty squares in the maze contains a piece of cheese. The
# mouse's goal is to reach that square without visiting the same square
# twice. The mouse can only move between neighboring squares. Since the
# mouse has been listening to classical music for a week, he is extremely
# intelligent and guaranteed to achieve his goal.

# As the mouse moves from his starting point to the cheese, he may
# encounter some squares where he must choose between several neighboring
# squares to continue. This happens when the mouse steps into a square
# which has more than one neighboring empty square, excluding the square
# from which he came, or when he has more than one neighboring empty
# square at the start. These situations are called "decisions" and the
# mouse will always make the right choice.

# You are given a String[] maze representing the maze. It contains N
# elements, each containing M characters. Empty squares are denoted by
# '.', walls are denoted by uppercase 'X', the mouse's starting point is
# denoted by 'M', and the square containing the cheese is denoted by '*'.
# Return the number of decisions the mouse will make on his way to the
# cheese.
from collections import deque


class MazeWanderingEasy(object):
    def decisions(self, maze):
        N = len(maze)
        M = len(maze[0])
        decision_count = [[0] * M for _ in xrange(N)]
        mouse = find_mouse(maze)
        Q = deque([mouse])
        seen = set([mouse])
        while Q:
            i, j = Q.popleft()
            if maze[i][j] == "*":
                return decision_count[i][j]
            neighbours = filter(lambda x: x not in seen, get_valid_neighbours(i, j, maze))
            if len(neighbours) > 1:
                decision_count[i][j] += 1
            for i2, j2 in neighbours:
                seen.add((i2, j2))
                Q.append((i2, j2))
                decision_count[i2][j2] = decision_count[i][j]
        return -1


def find_mouse(maze):
    for i in xrange(len(maze)):
        for j in xrange(len(maze[i])):
            if maze[i][j] == "M":
                return i, j
    return None

def get_valid_neighbours(i, j, maze):
    N = len(maze)
    M = len(maze[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    neighbours = []
    for x, y in zip(dx, dy):
        if 0 <= i + x < N and 0 <= j + y < M:
            if maze[i + x][j + y] != "X":
                neighbours.append((i + x, j + y))
    return neighbours


if __name__ == '__main__':
    print MazeWanderingEasy().decisions(["*.M"])
