class TCU(object):
    def majors(self, percentages, start, years):
        n = len(percentages)
        percentages = [map(int, x.split()) for x in percentages]
        for year in xrange(years):
            new = [0] * n
            for i, population in enumerate(start):
                migrants = 0
                for j in xrange(n):
                    if i != j:
                        new[j] += percentages[i][j] * population / 100
                        migrants += percentages[i][j] * population / 100
                # Don't bother dealing with floats, just calculate the
                # number staying in major by subtracting number migrating.
                new[i] += start[i] - migrants
            start = new
        return start


# WORKS BUT SLOWER
# import re
# import math


# def memoize(fn):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         key = str(args) + str(kwargs)
#         if key not in cache:
#             cache[key] = fn(*args, **kwargs)
#         return cache[key]
#     return wrapper


# class TCU(object):
#     def majors(self, percentages, start, years):
#         current = start
#         percentages = [map(lambda x: int(x) / 100.0, re.findall("[0-9]+", x)) for x in percentages]
#         # print percentages
#         for year in xrange(years):
#             current = self.new_year(current, percentages)
#         return current

#     @memoize
#     def new_year(self, current, percentages):
#         new = [0] * len(percentages)
#         for i, population in enumerate(current):
#             for j in xrange(len(percentages)):
#                 switch = math.modf(percentages[i][j] * population)
#                 new[j] += switch[1]
#                 new[i] += switch[0]
#         return map(int, map(round, new))

# print TCU().majors(["80 1 5 14", "2 76 19 3", "1 3 45 51", "30 32 26 12"], [1237, 625, 9618, 134760], 500)

print TCU().majors(["7 3 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ", "5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 "], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 10000)
