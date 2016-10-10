class WeirdRooks(object):
    def describe(self, cols):
        n = len(cols)
        self.cols = cols
        # exists_arrangement[rooks][specials] will be True or False depending on if
        # an arrangement on the board with rooks and specials exists.
        self.exists_arrangement = [[False] * (n * 10 + 1) for _ in xrange(n + 1)]
        # Solve from bottom row up.
        self.solve(n - 1, 0, 0, 0)
        pairs = []
        for rooks in xrange(len(self.exists_arrangement)):
            for specials in xrange(len(self.exists_arrangement[0])):
                if self.exists_arrangement[rooks][specials]:
                    pairs.append("%d,%d" % (rooks, specials))
        return " ".join(pairs)

    def solve(self, row, below, rooks, specials):
        if row == -1:
            # Reached end of board.
            self.exists_arrangement[rooks][specials] = True
            return
        # i represnts the position in the row we place a rook
        # -1 means we don't place a rook in this row.
        for i in xrange(-1, self.cols[row]):
            row_specials = 0
            # Loop through squares to the right and count how many are special.
            for j in xrange(i + 1, self.cols[row]):
                if below & (1 << j) == 0:
                    # This square is special.
                    row_specials += 1
            if i == -1:
                # Move to next row without adding a rook.
                self.solve(row - 1, below, rooks, specials + row_specials)
            elif below & (1 << i) == 0:
                # This square is free for a rook.
                self.solve(row - 1, below | 1 << i, rooks + 1, specials + row_specials)


class WeirdRooks2(object):
    # This works but does not scale well. (exponential)
    def describe(self, cols):
        pairs = set()
        for rooks, board in get_arrangements(cols):
            special = count_special(board)
            pairs.add((rooks, special))
        pairs = sorted(pairs)
        pairs = ["%d,%d" % (pair[0], pair[1]) for pair in pairs]
        return " ".join(pairs)


def get_arrangements(cols):
    """Gets valid arrangements of rooks on the board defined by cols.

    Returns a list of tuple pairs with the number of rooks in the arrangement
    and the board representing the arrangement with 1s for rooks and 0s for
    unoccupied squares.
    """
    board = [[0] * col for col in cols]
    solutions = []
    _get_arrangements(board, cols, solutions)
    return solutions


def _get_arrangements(board, cols, solutions, i=0, blocked=[], rooks=0):
    if i == len(cols):
        solutions.append((rooks, board))
        return
    # Arrangement where this row has no rooks.
    _get_arrangements(board, cols, solutions, i + 1, blocked, rooks)
    # Arrangements where this row has a rook.
    for j in xrange(cols[i]):
        if j not in blocked:
            new_board = [list(row) for row in board]
            new_board[i][j] = 1
            new_blocked = list(blocked)
            new_blocked.append(j)
            _get_arrangements(new_board, cols, solutions, i + 1, new_blocked, rooks + 1)


def count_special(board):
    """Counts the number of special squares in the board."""
    special = 0
    blocked_cols = set()
    # Work in reverse direction from bottom right.
    for i in reversed(xrange(len(board))):
        for j in reversed(xrange(len(board[i]))):
            if board[i][j] == 0 and j not in blocked_cols:
                    special += 1
            elif board[i][j] == 1:
                # No further squares in this row can be special.
                blocked_cols.add(j)
                break
    return special

if __name__ == '__main__':
    # print WeirdRooks().describe([3, 3, 3])
    print WeirdRooks().describe([10] * 7)
