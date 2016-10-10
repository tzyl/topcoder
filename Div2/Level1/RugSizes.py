# Rugs come in various sizes. In fact, we can find a rug with any integer
# width and length, except that no rugs have a distinct width and length
# that are both even integers. For example, we can find a 4x4 rug, but not
# a 2x4 rug. We want to know how many different choices we have for a
# given area.

# Create a class RugSizes the contains a method rugCount that is given the
# desired area and returns the number of different ways in which we can
# choose a rug size that will cover that exact area. Do not count the same
# size twice -- a 6 x 9 rug and a 9 x 6 rug should be counted as one
# choice.


class RugSizes(object):
    def rugCount(self, area):
        count = 0
        x = 1
        while x * x <= area:
            if area % x == 0:
                y = area / x
                if not (x != y and x % 2 == 0 and y % 2 == 0):
                    count += 1
            x += 1
        return count
