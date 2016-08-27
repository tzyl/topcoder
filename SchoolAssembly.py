import math


class SchoolAssembly(object):
    def getBeans(self, kids, quantity):
        return int(math.ceil(((kids - 1) * quantity + (quantity - 1) * 5 + 1) / float(20)))
