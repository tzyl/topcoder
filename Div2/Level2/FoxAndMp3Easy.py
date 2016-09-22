class FoxAndMp3Easy(object):
    def playList(self, n):
        songs = []
        for i in xrange(1, n + 1):
            songs.append(str(i) + ".mp3")
        songs.sort()
        return songs[:50]

if __name__ == '__main__':
    print FoxAndMp3Easy().playList(101)
