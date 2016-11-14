# Wolf Sothe and Cat Snuke are playing a card game. The game is played
# with exactly 100 cards. The cards are numbered from 1 to 100. The game
# is played as follows:

# 1. First, Cat Snuke chooses the goal: an integer N between 1 and 100,
# inclusive.
# 2. Then, Wolf Sothe chooses exactly K of the 100 cards and gives the chosen
# cards to Snuke.
# 3. Next, Cat Snuke may throw some of those K cards away. He may choose any
# subset of cards he was given, possibly none or all of them.
# 4. Finally, Cat Snuke may write minus signs onto any subset of the cards he
# still holds. For example, if he currently has the cards {1,3,4,7}, he
# may alter them to {-1,3,4,-7}.

# At the end of the game, Snuke computes the sum of the numbers on his
# cards (with the added minus signs). Snuke wins the game if the sum is
# exactly equal to the goal number N. Otherwise, Sothe wins.

# Your task is to help Wolf Sothe win the game. We are now in step 2 of
# the game. You are given the N chosen by Snuke and the K that specifies
# the number of cards you have to give to Snuke. Choose those K cards in
# such a way that Snuke will be unable to win the game. If you can do
# that, return a with K elements: the numbers on the chosen cards. If
# there are multiple solutions, you may return any of them. If there is no
# solution, return an empty instead.


class WolfCardGame(object):
    def createAnswer(self, N, K):
        for i in xrange(2, 6):
            if N % i != 0:
                return [i * j for j in xrange(1, K + 1)]
        return [1] + [7 * i for i in xrange(1, K)]


if __name__ == '__main__':
    print WolfCardGame().createAnswer(20, 4)
    print WolfCardGame().createAnswer(40, 1)
    print WolfCardGame().createAnswer(97, 6)
    print WolfCardGame().createAnswer(2, 12)
    print WolfCardGame().createAnswer(1, 2)
