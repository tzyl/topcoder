class AbsSequence(object):
    def getElements(self, first, second, indices):
        pass
        S = self.makeSequence(first, second, indices)
        return map(str, [S[index] for index in map(int, indices)])

    def makeSequence(self, first, second, indices):
        S = [int(first), int(second)]
        for index in map(int, indices):
            a = S[-2]
            b = S[-1]
            while index >= len(S):
                # Need to calculate up to index's value in S.
                a, b = b, abs(a - b)
                S.append(b)
        return S


test = AbsSequence()
print test.getElements("0", "0", ["1000000000000000000"])
