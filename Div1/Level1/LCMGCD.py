# You are given the x: a list containing n integers. Each element of x is
# a positive integer of the form 2^a * 3^b, where a and b are some
# nonnegative integers. The elements of x are not necessarily distinct.

# You are going to perform n-1 operations. Each operation will consist of
# the following steps:

# Choose two distinct indices into your list. Let X and Y be the numbers
# at those indices. Remove both of them from the list. (Note that X and Y
# are allowed to have the same value.)

# Compute one of two possible values: either the greatest common divisor
# (gcd) of X and Y, or the least common multiple (lcm) of X and Y.

# Append the computed value to your list.

# Obviously, after n-1 operations you will be left with a single integer.
# In addition to x you are given the t. You would like to know whether it
# is possible to perform the sequence of operations on x in such a way
# that the final integer will be t. If it is possible, return "Possible",
# otherwise return "Impossible".


class LCMGCD(object):
    def isPossible(self, x, t):
        # Reduce states to 0, 1 or 2 depending on whether the corresponding
        # target is less than equal to or greater than the target power.
        states = [(i, j) for i in xrange(3) for j in xrange(3)]
        initial_state = [0] * 9
        for n in x:
            a, b = reduce_state(n, t)
            if not initial_state[3*a + b] or (a, b) == (1, 1):
                initial_state[3*a + b] += 1
        # DFS on states to see if possible.
        stack = [tuple(initial_state)]
        seen = set(stack)
        while stack:
            state = stack.pop()
            if state == (0, 0, 0, 0, 1, 0, 0, 0, 0):
                return "Possible"
            # Pick two non zero elements in the state.
            for a, b in states:
                if state[3*a + b]:
                    for c, d in states:
                        if state[3*c + d]:
                            for i in xrange(2):
                                # Loop twice: once for lcm, once for gcd.
                                # Convert to list so we can mutate.
                                new_state = list(state)
                                new_state[3*a + b] -= 1
                                new_state[3*c + d] -= 1
                                if new_state[3*a + b] < 0:
                                    # Chose two of the same which were invalid.
                                    continue
                                if i == 0:
                                    s, t = max(a, c), max(b, d)
                                else:
                                    s, t = min(a, c), min(b, d)
                                new_state[3*s + t] += 1
                                # Convert to tuple for hashing.
                                new_state = tuple(new_state)
                                if new_state not in seen:
                                    seen.add(new_state)
                                    stack.append(new_state)
        return "Impossible"


def reduce_state(n, t):
    """Reduces to a state of (a, b) where a, b = 0, 1 or 2 depending on whether
    the power in n is less than equal to or greater than the target power in t.
    """
    a, b = find_powers(t)
    c, d = find_powers(n)
    x = 1 if c == a else 2 if c > a else 0
    y = 1 if d == b else 2 if d > b else 0
    return (x, y)


def find_powers(x):
    """Finds the powers of 2 and 3 of x."""
    a = 0
    while x % 2 == 0:
        a += 1
        x /= 2
    b = 0
    while x % 3 == 0:
        b += 1
        x /= 3
    return a, b


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


if __name__ == '__main__':
    print LCMGCD().isPossible([2, 3], 6)
    print LCMGCD().isPossible([4, 9], 6)
