class ABoardGame(object):
    def whoWins(self, board):
        self.board = board
        self.N = len(self.board) / 2
        n = 1
        while n <= self.N:
            alice = sum(self.board[i][j] == "A" for i, j in self.get_regions(n))
            bob = sum(self.board[i][j] == "B" for i, j in self.get_regions(n))
            if alice > bob:
                return "Alice"
            elif bob > alice:
                return "Bob"
            n += 1
        return "Draw"

    def get_regions(self, n):
        """
        Gets coordinates for Region n of the board. Returns an empty list if
        n is out of range of the board size
        """
        coords = []
        i = j = self.N - n
        for _ in xrange(2 * n - 1):
            j += 1
            coords.append((i, j))
        for _ in xrange(2 * n - 1):
            i += 1
            coords.append((i, j))
        for _ in xrange(2 * n - 1):
            j -= 1
            coords.append((i, j))
        for _ in xrange(2 * n - 1):
            i -= 1
            coords.append((i, j))
        return coords
