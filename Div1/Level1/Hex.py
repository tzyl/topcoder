class Hex(object):
    def picture(self, n, marks):
        board = self.draw_board(n)
        for mark in marks:
            self.mark_hexagon(mark, board)
        return board

    def draw_board(self, n):
        """Draws an nxn hex board."""
        board = [" _"]
        row = "/ \\_"
        i = 1
        while i < 3*n:
            board.append(row)
            i += 1
            if i < 2*n + 1:
                if i % 2 == 0:
                    row = "\\_" + row
                else:
                    row = "/ " + row
            else:
                row = "  " + row

            if len(row) > 2*n + 1:
                row = row[:2*n + 1]
            row = "" + row
        return board

    def mark_hexagon(self, mark, board):
        """
        Marks the hex board depending on coordinates and type of marker in mark
        where mark is a string of length 3 with the diagonal coordinate,
        vertical coordinate and mark type 'v' or 'h'.
        """
        # Extract diagonal coordinate, vertical coordinate and mark type.
        d = int(mark[0])
        v = int(mark[1])
        m = mark[2]
        row_idx = 1 + d + 2*v
        board[row_idx] = board[row_idx][:1 + 2*d] + m + board[row_idx][1 + 2*d + 1:]


if __name__ == '__main__':
    hex_game = Hex()
    print "\n".join(hex_game.picture(3, ["00v", "01v", "02v", "11h", "21h"]))
