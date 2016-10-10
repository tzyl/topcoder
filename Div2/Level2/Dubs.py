class Dubs(object):
    def count(self, L, R):
        # Every full 100 has 10 doubles.
        L_count = (L - 1) / 100 * 10 + ((L - 1) % 100) / 11
        R_count = R / 100 * 10 + (R % 100) / 11
        return R_count - L_count


if __name__ == '__main__':
    print Dubs().count(49, 101)
