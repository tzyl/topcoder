class DevuAndGame(object):
    def canWin(self, nextLevel):
        seen = set()
        location = 0
        while location not in seen and location != -1:
            seen.add(location)
            location = nextLevel[location]
        return "Win" if location == -1 else "Lose"
