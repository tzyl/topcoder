# The ice hockey season is almost over. Wolf Sothe and his teammates have
# asked Cat Snuke to take photos of their team.

# There are 2*N wolves on the ice hockey team. The wolves are numbered
# from 0 to 2*N-1.

# Cat Snuke is going to take photos of the whole team. The photos all have
# to look nice and they all have to look different. Both "nice" and
# "different" are formally defined below.

# While taking each photo, the wolves will stand in a grid pattern with
# two rows by N columns. There is only one constraint: each row of the
# grid must contain a wolf whose number is K or more. Any such arrangement
# of wolves will look nice in a photo.

# Given a photo of our 2*N wolves, we can look at it and write down a
# sequence of N+2 integers:

# For each column (from the left to the right), write down the largest
# wolf number in that column.
# Write down the largest wolf number in the first row.
# Write down the largest wolf number in the second row.
# Two photos are considered different if they produce different sequences.

# You are given the s N and K. Let X be the maximal number of nice and
# pairwise different photos Cat Snuke can take. Compute and return the
# value (X modulo 1,000,000,007).


class WolfHockeyTeamEasy(object):
    cache = {}

    def count(self, N, K):
        answer = 0
        # Populate cache so we don't hit recursion depth.
        for x in xrange(2 * N):
            for y in xrange(x):
                ways = self.f(x, y)
                if x == 2 * N - 1 and y >= K:
                    # This is a valid pair of (x, y).
                    answer = (answer + ways) % 1000000007
        # There are n! possible arrangements of the columns of each sorted
        # sequence and 2! possible arrangements of the rows.
        for i in xrange(2, N + 1):
            answer = (answer * i) % 1000000007
        answer = (answer * 2) % 1000000007
        return answer

    def f(self, x, y):
        """Returns the number of possible valid sequences assuming the rows and
        columns are sorted with x > y the largest elements in each of the rows.
        """
        if (x, y) not in self.cache:
            if x == 1 and y <= 1:
                self.cache[(x, y)] = 1
            elif y == 0 or y > x:
                self.cache[(x, y)] = 0
            else:
                self.cache[(x, y)] = self.f(x - 2, y - 1) + self.f(x, y - 1) % 1000000007
        return self.cache[(x, y)]


# def memoize(fn):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         key = str(args) + str(kwargs)
#         if key not in cache:
#             cache[key] = fn(*args, **kwargs)
#         return cache[key]
#     return wrapper


# @memoize
# def f(x, y):
#     """Returns the number of possible valid sequences assuming the rows and
#     columns are sorted with x > y the largest elements in each of the rows.
#     """
#     if x == 1 and y <= 1:
#         return 1
#     elif y == 0 or y > x:
#         return 0
#     else:
#         return f(x - 2, y - 1) + f(x, y - 1) % 1000000007


if __name__ == '__main__':
    print WolfHockeyTeamEasy().count(2, 0)
    print WolfHockeyTeamEasy().count(4, 5)
    print WolfHockeyTeamEasy().count(100, 120)
    print WolfHockeyTeamEasy().count(234, 467)
    print WolfHockeyTeamEasy().count(810, 897)
