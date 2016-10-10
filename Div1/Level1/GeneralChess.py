class GeneralChess(object):
    def attackPositions(self, pieces):
        all_vulnerable = []
        diff = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        for piece in pieces:
            x, y = map(int, piece.split(","))
            vulnerable = []
            for dx, dy in diff:
                vulnerable.append((x + dx, y + dy))
            all_vulnerable.append(vulnerable)
        attack = [position for position in all_vulnerable[0] if
                  all(position in vulnerable for vulnerable in all_vulnerable)]
        attack.sort()
        return ["%d,%d" % (pos[0], pos[1]) for pos in attack]

if __name__ == '__main__':
    print GeneralChess().attackPositions(["0,0"])
    print GeneralChess().attackPositions(["-1000,1000", "-999,999", "-999,997"])
