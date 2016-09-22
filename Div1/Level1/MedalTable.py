from collections import defaultdict


class MedalTable(object):
    def generate(self, results):
        countries = defaultdict(lambda: [0, 0, 0])
        results = [result.split() for result in results]
        for result in results:
            countries[result[0]][0] += 1
            countries[result[1]][1] += 1
            countries[result[2]][2] += 1
        countries = countries.items()
        countries.sort(cmp=self.compare_countries)
        return map(lambda c: "%s %d %d %d" % (c[0], c[1][0], c[1][1], c[1][2]), countries)

    def compare_countries(self, c1, c2):
        if c1[1][0] != c2[1][0]:
            return -1 if c1[1][0] > c2[1][0] else 1
        elif c1[1][1] != c2[1][1]:
            return -1 if c1[1][1] > c2[1][1] else 1
        elif c1[1][2] != c2[1][2]:
            return -1 if c1[1][2] > c2[1][2] else 1
        elif c1[0] != c2[0]:
            return -1 if c1[0] < c2[0] else 1
        return 0

if __name__ == '__main__':
    print MedalTable().generate(["ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"])
