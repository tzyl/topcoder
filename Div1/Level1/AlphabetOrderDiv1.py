# The ancient civilization of Nlogonia used the same 26 letters as modern
# English: 'a'-'z'. However, we do not know the order in which these
# letters appeared in the Nlogonian alphabet.

# One particular custom in Nlogonia was that in a good word the letters
# appear in non-decreasing order. For example, in English the word "ciel"
# is not a good word because in the alphabet 'i' is after 'e'. The word
# "ceil" is a good word because 'c' <= 'e' <= 'i' <= 'l'.

# You are given the String[] words. Each element of words is a nonempty
# string of lowercase English letters. Return "Possible" if it is possible
# that all elements of words were good words in Nlogonian, and
# "Impossible" otherwise.

# In other words, return "Possible" if and only if there is at least one
# possible Nlogonian alphabet such that the letters of each word in words
# are in non-decreasing alphabetical order.
from collections import defaultdict
from itertools import combinations
import string


class AlphabetOrderDiv1(object):
    def isOrdered(self, words):
        comes_after = defaultdict(set)
        for word in words:
            for c1, c2 in combinations(word, 2):
                if c1 != c2:
                    comes_after[c1].add(c2)

        # Look for cycles using DFS. Impossible if we find a cycle.
        def dfs_visit(v):
            seen.add(v)
            for u in comes_after[v]:
                if u in seen and u not in finished:
                    self.possible = False
                elif u not in seen:
                    dfs_visit(u)
            finished.add(v)

        seen = set()
        finished = set()
        self.possible = True

        for c in string.lowercase:
            if c not in seen:
                dfs_visit(c)
        return "Possible" if self.possible else "Impossible"

    def isOrdered2(self, words):
        comes_after = defaultdict(set)
        for word in words:
            for c1, c2 in combinations(word, 2):
                if c1 != c2:
                    comes_after[c1].add(c2)

        # Calculate strongly connected components.
        # If we find less than 26 SCCs then impossible.
        def dfs_visit(v):
            seen.add(v)
            for u in comes_after[v]:
                if u not in seen:
                    dfs_visit(u)
            finished.append(v)

        seen = set()
        finished = []

        for c in string.lowercase:
            if c not in seen:
                dfs_visit(c)

        rooted = set()
        scc = []

        while finished:
            root = finished.pop()
            if root not in rooted:
                # New strongly connected component.
                component = []
                rooted.add(root)
                stack = [root]
                while stack:
                    a = stack.pop()
                    component.append(a)
                    for b in string.lowercase:
                        if b not in rooted and a in comes_after[b]:
                            rooted.add(b)
                            stack.append(b)
                scc.append(component)

        return "Possible" if len(scc) == 26 else "Impossible"


if __name__ == '__main__':
    print AlphabetOrderDiv1().isOrdered2(["single", "round", "match"])
    print AlphabetOrderDiv1().isOrdered2(["topcoder", "topcoder"])
    print AlphabetOrderDiv1().isOrdered2(["a" * 100] * 100)
