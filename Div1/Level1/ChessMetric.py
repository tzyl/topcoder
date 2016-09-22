class ChessMetric(object):
    # Branch and bound approach. Ignore contributions from positions that are
    # too far to affect the solution.
    def howMany(self, size, start, finish, numMoves):
        board = [[0] * size for _ in xrange(size)]
        board[start[0]][start[1]] = 1
        bounds = self.create_bounds_board(size, finish[0], finish[1])
        dx = [1, 1, 1, 0, -1, -1, -1, 0, 1, 2, 2, 1, -1, -2, -2, -1]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
        for move in xrange(numMoves):
            new_board = [[0] * size for _ in xrange(size)]
            for i in xrange(size):
                for j in xrange(size):
                    if bounds[i][j] <= numMoves - move:
                        for m, n in zip(dx, dy):
                            if 0 <= i + m < size and 0 <= j + n < size:
                                new_board[i][j] += board[i + m][j + n]
            board = new_board
        return board[finish[0]][finish[1]]

    # Creates a board where the entries are the minimum number of moves we need
    # to move from that position to the destination point (i, j).
    def create_bounds_board(self, size, i, j):
        from math import sqrt, ceil
        bounds = [[0] * size for _ in xrange(size)]
        for m in xrange(size):
            y = i - m
            for n in xrange(size):
                x = j - n
                d = sqrt(x*x + y*y)
                bounds[m][n] = int(ceil(d / sqrt(5)))
        return bounds

    # Improve speed by completing half moves from destination and half from
    # source then join together.
    def howMany2(self, size, start, finish, numMoves):
        start_board = [[0] * size for _ in xrange(size)]
        end_board = [[0] * size for _ in xrange(size)]
        start_board[start[0]][start[1]] = 1
        end_board[finish[0]][finish[1]] = 1
        for _ in xrange(numMoves / 2):
            start_board = self.advance_board(start_board)
            end_board = self.advance_board(end_board)
        if numMoves % 2 == 1:
            start_board = self.advance_board(start_board)
        total = 0
        for i in xrange(size):
            for j in xrange(size):
                total += start_board[i][j] * end_board[i][j]
        return total
        # return sum(start_board[i][j]*end_board[i][j] for i in xrange(size) for j in xrange(size))

    def advance_board(self, board):
        dx = [1, 1, 1, 0, -1, -1, -1, 0, 1, 2, 2, 1, -1, -2, -2, -1]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
        size = len(board)
        new_board = [[0] * size for _ in xrange(size)]
        for i in xrange(size):
            for j in xrange(size):
                for m, n in zip(dx, dy):
                    if 0 <= i + m < size and 0 <= j + n < size:
                        new_board[i][j] += board[i + m][j + n]
        return new_board

    # This works but is just a bit too slow.
    def howMany3(self, size, start, finish, numMoves):
        board = [[0] * size for _ in xrange(size)]
        dx = [1, 1, 1, 0, -1, -1, -1, 0, 1, 2, 2, 1, -1, -2, -2, -1]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
        board[finish[0]][finish[1]] = 1
        for _ in xrange(numMoves):
            new_board = [[0] * size for _ in xrange(size)]
            for i in xrange(size):
                for j in xrange(size):
                    for m, n in zip(dx, dy):
                        if 0 <= i + m < size and 0 <= j + n < size:
                            new_board[i][j] += board[i + m][j + n]
                    # new_board[i][j] = sum(
                    #     board[m][n] for m, n in self.get_neighbours(i, j, size)
                    # )
            board = new_board
        return board[start[0]][start[1]]

    # def get_neighbours(self, i, j, size):
    #     for m in xrange(i - 2, i + 3):
    #         for n in (j - 1, j + 1):
    #             if 0 <= m < size and 0 <= n < size:
    #                 yield m, n
    #     for m in (i - 1, i + 1):
    #         for n in (j - 2, j, j + 2):
    #             if 0 <= m < size and 0 <= n < size:
    #                 yield m, n

if __name__ == '__main__':
    print ChessMetric().howMany(2, (0, 0), (0, 1), 1)
    print ChessMetric().howMany(100, (0, 0), (0, 99), 50)
