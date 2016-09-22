# Gumi loves singing. She knows N songs. The songs are numbered 0 through N-1. She now has some time and she would love to sing as many different songs as possible.
# You are given a duration. For each i, duration[i] is the duration of song i in Gumi's time units.
# Gumi finds it difficult to sing songs with quite different tones consecutively. You are given a tone with the following meaning: If Gumi wants to sing song y immediately after song x, she will need to spend |tone[x]-tone[y]| units of time resting between the two songs. (Here, || denotes absolute value.)
# You are also given an T. Gumi has T units of time for singing. She can start singing any song she knows immediately at the beginning of this time interval. Compute the maximal number of different songs she can sing completely within the given time.


class GUMIAndSongsDiv1(object):
    # Dynamic programming O(n^3). Considers all possible tone ranges and
    # greedily chooses the shortest songs as possible in each tone range.
    def maxSongs(self, duration, tone, T):
        n = len(duration)
        songs = zip(tone, duration)
        songs.sort()
        best = 0
        for i in xrange(n):
            for j in xrange(i, n):
                tone_range = songs[j][0] - songs[i][0]
                t = T - tone_range
                greedy_songs = songs[i:j+1]
                greedy_songs.sort(key=lambda s: s[1])
                total = 0
                for song in greedy_songs:
                    if song[1] <= t:
                        total += 1
                        t -= song[1]
                best = max(best, total)
        return best

    # Initial thoughts. Not working.
    # Greedy algorithm tried from each song as start.
    def maxSongs2(self, duration, tone, T):
        best = 0
        n = len(duration)
        # Try each song as start.
        for i in xrange(n):
            if duration[i] > T:
                continue
            t = T - duration[i]
            total = 1
            unused = zip(duration, tone)
            unused.pop(i)
            prev_tone = tone[i]
            while unused:
                unused.sort(key=lambda s: s[0] + abs(s[1] - prev_tone))
                greedy_choice = unused[0][0] + abs(unused[0][1] - prev_tone)
                if greedy_choice > t:
                    break
                total += 1
                t -= greedy_choice
                prev_tone = unused.pop(0)[1]
            best = max(best, total)
            if best == n:
                return n
        return best

if __name__ == '__main__':
    print GUMIAndSongsDiv1().maxSongs([3, 5, 4, 11], [2, 1, 3, 1], 17)
    print GUMIAndSongsDiv1().maxSongs([5611,39996,20200,56574,81643,90131,33486,99568,48112,97168,5600,49145,73590,3979,94614],[2916,53353,64924,86481,44803,61254,99393,5993,40781,2174,67458,74263,69710,40044,80853],302606)
