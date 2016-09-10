class Ordered(object):
    def getType(self, values):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        outcomes = ["DESCENDING", "NONASCENDING", "ASCENDING", "NONDESCENDING"]
        ascending = None
        consecutive_max = 1
        consecutive = 1
        total = values[0]
        prev = values[0]
        for value in values[1:]:
            if value == prev:
                consecutive += 1
                consecutive_max = max(consecutive_max, consecutive)
            elif value != prev:
                consecutive = 1
                if ascending is None:
                    ascending = value > prev
                elif ascending != (value > prev):
                    return "NOTHING"
            total += value
            prev = value

        if ascending is None:
            return "NOTHING"
        elif consecutive_max > 1:
            return "%s %s" % (outcomes[2*int(ascending) + 1], consecutive_max)
        else:
            x = gcd(total, len(values))
            numerator, denominator = total / x, len(values) / x
            return "%s %s/%s" % (outcomes[2*int(ascending)], numerator, denominator)

print Ordered().getType([1, 2, 4, 11])
print Ordered().getType([2, 2, 2, 2, 2])
