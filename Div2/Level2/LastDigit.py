class LastDigit(object):
    def findX(self, S):
        n = len(str(S))
        X_digits = [0] * n
        i = 0
        while S and i < n:
            X_digits[i] = min(S / sum(10**j for j in xrange(n - i)), 9)
            S -= X_digits[i] * sum(10**j for j in xrange(n - i))
            i += 1
        if S:
            return -1
        return int("".join(map(str, X_digits)))


def calculate_sum(digits):
    total = 0
    for i in xrange(1, len(digits) + 1):
        total += int("".join(map(str, digits[:i])))
    return total

if __name__ == '__main__':
    # print LastDigit().calculate_sum([5, 0, 9])
    print LastDigit().findX(564)
    print LastDigit().findX(1000000000000000000)
    print LastDigit().findX(837592744927492746)
    print LastDigit().findX(11111)
    print LastDigit().findX(10)
