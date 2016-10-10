# A few days ago, you won a tour of a textile factory. (Chocolate factory
# tours were deemed too risky to children and therefore banned). As
# everyone knows, textile is made of strings, so it's time to solve a
# string problem!


# You are given a S of length L. For any string T, we can now define its
# covering number c(T) as the maximum number of non-overlapping
# occurrences of S in T. Each occurrence must be a contiguous substring of
# T, and they may not share any letters.


# Examples:
# If S="ab", we have c("xyz")=0 and c("ababxab")=3.
# If S="aaa", we have c("aa")=0 and c("aaaaaa")=2.


# In addition to S, you are given two s N and K.


# Consider all strings with the following properties:

# Each character of the string is a lowercase English letter ('a'-'z').
# The length of the string is between L*K and L*K+N, inclusive.
# The covering number of the string is exactly K.
# Let X be the number of strings with the above properties. Since X may be
# large, compute and return the value (X modulo 1,000,000,009).


def memoize(fn):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    return wrapper


class LinenCenterEasy(object):
    # O(LKN) where L = len(S)
    def countStrings(self, S, N, K):
        self.prefix_becomes = calculate_prefix_changes(S)
        self.bad_prefix = calculate_bad_prefixes(S)
        return self.f(S, N, K, 0)

    @memoize
    def f(self, S, N, K, p):
        """Returns the number of ways of filling between LK and LK + N remaining
        characters. The last p characters are extra characters equal to the
        prefix of length p of S.
        """
        if p == len(S):
            return 0
        result = 0
        if K == 0:
            result += 1
        elif K > 0 and not self.bad_prefix[p]:
            # Start a new instance of S here.
            result += self.f(S, N, K - 1, 0)
        if N > 0:
            # Don't start a new instance of S here instead add one of the
            # remaining chars.
            for c in "abcdefghijklmnopqrstuvwxyz":
                result += self.f(S, N - 1, K,
                                 self.prefix_becomes[p][ord(c) - ord("a")])
        return result % 1000000009

    # Simplification if K = 0.
    def g(self, S, N, p):
        """"Returns the number of ways to fill up to N remaining characters of a
        string so that the final string doesn't include S as a substring assuming
        the last p current characters are a prefix of S of length p.
        """
        if p == len(S):
            return 0
        result = 0
        if N > 0:
            # The current string is safe so we could just stop here.
            result += 1
        for c in "abcdefghijklmnopqrstuvwxyz":
            result += self.g(S, N - 1,
                             self.prefix_becomes[p][ord(c) - ord("a")])
        return result


def calculate_prefix_changes(S):
    """Returns a list prefix_becomes where prefix_becomes[p][c] gives the value
    of the maximum length prefix of S at the end of the currently built string
    with c added to the end.
    """
    prefix_becomes = [[0] * 26 for _ in xrange(len(S))]
    # We can only transition from p = 0 to p = 1 if c is the first char of S.
    prefix_becomes[0][ord(S[0]) - ord("a")] = 1
    for p in xrange(1, len(S)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            new_s = S[:p] + c
            new_p = p + 1
            while new_p > 0:
                if new_s.endswith(S[:new_p]):
                    break
                new_p -= 1
            prefix_becomes[p][ord(c) - ord("a")] = new_p
    return prefix_becomes


def calculate_bad_prefixes(S):
    """bad_prefix[p] is True if it is not safe to insert S immediately after a
    prefix of length p.
    """
    bad_prefix = [False] * len(S)
    for p in xrange(1, len(S)):
        if S[:p] + S[:len(S) - p] == S:
            bad_prefix[p] = True
    return bad_prefix


if __name__ == '__main__':
    print LinenCenterEasy().countStrings("xy", 2, 1)
    print LinenCenterEasy().countStrings("ababab", 5, 4)
