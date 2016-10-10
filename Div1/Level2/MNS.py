class MNS(object):
    def combos(self, numbers):
        magic = []
        for p in permutations(numbers):
            if p not in magic:
                if p[0] + p[1] + p[2] == p[3] + p[4] + p[5] == p[6] + p[7] + p[8] == p[0] + p[3] + p[6] == p[1] + p[4] + p[7] == p[2] + p[5] + p[8]:
                    magic.append(p)
        return len(magic)


def permutations(numbers):
    if len(numbers) <= 1:
        yield numbers
    else:
        for p in permutations(numbers[1:]):
            for i in xrange(len(numbers)):
                yield p[:i] + [numbers[0]] + p[i:]

if __name__ == '__main__':
    print MNS().combos([1, 2, 3, 3, 2, 1, 2, 2, 2])
    print MNS().combos([4] * 9)
    print MNS().combos([1, 5, 1, 2, 5, 6, 2, 3, 2])
    print MNS().combos([1, 2, 6, 6, 6, 4, 2, 6, 4])
