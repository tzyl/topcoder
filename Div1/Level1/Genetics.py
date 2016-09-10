class Genetics(object):
    def getOffspring(self, g1, g2, dom):
        properties = []
        for c1, c2, d in zip(g1, g2, dom):
            if c1.isupper() == c2.isupper():
                # Both upper or both lower.
                properties.append(c1)
            elif d == "D":
                properties.append(c1.upper())
            elif d == "R":
                properties.append(c1.lower())
        return "".join(properties)

print Genetics().getOffspring("MGskgzTFQoclnDjZu", "mgSKGzTFQoClnDJzU", "DDDDDRDDDDRDDDDDD")
