class UnsortedSequence(object):
    # O(nlg(n)) if comparison sort. O(n) if use counting sort.
    def getUnsorted(self, s):
        s.sort()
        last = len(s) - 1
        for i in reversed(xrange(len(s) - 1)):
            if s[i] != s[last]:
                s[i], s[last] = s[last], s[i]
                return s
            last = i
        return []

if __name__ == '__main__':
    print UnsortedSequence().getUnsorted([1, 2, 3, 4])
