class QuickSums(object):
    def minSums(self, numbers, sum):
        if int(numbers) == sum:
            return 0
        elif len(numbers) == 1:
            return -1
        best = -1
        for i in xrange(1, len(numbers)):
            x = self.minSums(numbers[i:], sum - int(numbers[:i]))
            if x != -1:
                if best == -1:
                    best = 1 + x
                else:
                    best = min(best, 1 + x)
        return best

if __name__ == '__main__':
    print QuickSums().minSums("99999", 45)  # 4
    print QuickSums().minSums("1110", 3)  # 3
    print QuickSums().minSums("0123456789", 45)  # 8
    print QuickSums().minSums("99999", 100)  # -1
    print QuickSums().minSums("382834", 100)  # 2
    print QuickSums().minSums("9230560001", 71)  # 4
    print QuickSums().minSums("1000000001", 11)  # 1
