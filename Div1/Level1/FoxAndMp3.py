class FoxAndMp3(object):
    def playList(self, n):
        songs = []
        for i in xrange(1, 10):
            self.add_suffixes(songs, i, n)
        return songs

    def add_suffixes(self, songs, k, n):
        if k > n or len(songs) == min(n, 50):
            return
        songs.append(str(k) + ".mp3")
        for i in xrange(10):
            self.add_suffixes(songs, k*10 + i, n)

if __name__ == '__main__':
    print FoxAndMp3().playList(1000000000)
