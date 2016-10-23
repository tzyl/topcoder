# Hero plays a game with a deck of cards and a counter. Initially, the
# counter is set to zero. During the game Hero must play each card in the
# deck exactly once. He gets to choose the order in which he plays the
# cards. You are given the description of the deck in the String s. Each
# character of s is either '+' or a digit ('0'-'9'). Each character
# represents one card, as described below.

# Whenever Hero plays a card with a '+', the counter is incremented.
# (I.e., its value is increased by 1.)

# Whenever Hero plays a card with a digit, he gets some (possibly zero)
# penalty points. The number of penalty points is calculated as abs(C -
# D), where C is the current value of the counter and D is the digit on
# the card.

# Hero wants to minimize the sum of penalty points he receives during the
# game. Find an order in which he should play the cards, and return that
# order in a String. If there are multiple optimal orders of cards, return
# the lexicographically smallest among them.


class Plusonegame(object):
    # Optimal order is to sort the digits and put one plus in between
    # differing groups of digits.
    def getorder(self, s):
        digit_counts = {x: 0 for x in xrange(10)}
        pluses_left = len(s)
        for c in s:
            if c != "+":
                digit_counts[int(c)] += 1
                pluses_left -= 1
        result = []
        for x in range(10):
            result.append(str(x) * digit_counts[x])
            if pluses_left:
                result.append("+")
                pluses_left -= 1
        if pluses_left:
            # Put the remaining pluses at the end.
            result.append("+" * pluses_left)
        return "".join(result)


if __name__ == '__main__':
    print Plusonegame().getorder("1++")
    print Plusonegame().getorder("549")
    print Plusonegame().getorder("++++++")
    print Plusonegame().getorder("+++++2+")
    print Plusonegame().getorder("++++4++++200++2++1+6++++++")
    print Plusonegame().getorder("++11199999")
