class DoubleString(object):
    def check(self, S):
        n = len(S)
        return "square" if S[:n/2] == S[n/2:] else "not square"
