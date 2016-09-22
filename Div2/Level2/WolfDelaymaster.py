class WolfDelaymaster(object):
    def check2(self, str):
        if not str:
            return "INVALID"
        i = 0
        while i < len(str):
            length = 0
            while i < len(str) and str[i] == "w":
                length += 1
                i += 1
            if not length or len(str) - i < 3 * length:
                return "INVALID"
            for c in ("o", "l", "f"):
                for _ in xrange(length):
                    if str[i] != c:
                        return "INVALID"
                    i += 1
        return "VALID"

    def check(self, str):
        if not str:
            return "INVALID"
        i = 0
        while i < len(str):
            w, o, l, f = 0, 0, 0, 0
            while i < len(str) and str[i] == "w":
                w += 1
                i += 1
            while i < len(str) and str[i] == "o":
                o += 1
                i += 1
            while i < len(str) and str[i] == "l":
                l += 1
                i += 1
            while i < len(str) and str[i] == "f":
                f += 1
                i += 1
            if not (w == o == l == f):
                return "INVALID"
        return "VALID"

if __name__ == '__main__':
    print WolfDelaymaster().check("owolf")  # False
    print WolfDelaymaster().check("wolfwwoollff")  # True
    print WolfDelaymaster().check("wolfolwolf")  # False
    print WolfDelaymaster().check("wwoollffw")  # False
    print WolfDelaymaster().check("woalf")  # False
    print WolfDelaymaster().check("wwwooolll")  # False
    print WolfDelaymaster().check("wwwooolllfff")  # True
    print WolfDelaymaster().check("")  # INVALID
