class ChessboardPattern(object):
    def makeChessboard(self, rows, columns):
        characters = [".", "X"]
        board = [[characters[(i + (rows - 1 - j)) % 2] for i in xrange(columns)] for j in xrange(rows)]
        return ["".join(row) for row in board]

if __name__ == '__main__':
    for row in ChessboardPattern().makeChessboard(8, 8):
        print row
