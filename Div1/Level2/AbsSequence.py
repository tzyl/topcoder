# Let's consider an infinite sequence S of non-negative integers defined
# as follows:

# S0 = first;
# S1 = second;
# Si = |Si-2 - Si-1| for all i >= 2.

# You will be given s first and second, representing the 0-th and the 1-st
# elements of the sequence S, and a indices, each element of which
# represents a non-negative integer without extra leading zeros. Return a
# containing as many elements as indices, where the i-th element is equal
# to the indices[i]-th element of the sequence S (index is 0-based). No
# element of the return should contain extra leading zeros.


class AbsSequence(object):
    def getElements(self, first, second, indices):
        return map(str, [find_in_sequence(int(first), int(second), i) for i in map(int, indices)])


def find_in_sequence(x, y, n):
    # Returns the nth element in the sequence generated with x and y as the
    # two starting values.
    if n < 2:
        # Simply return the corresponding starting element.
        return x if n == 0 else y
    if y == 0:
        return 0 if n % 3 == 1 else x
    if x <= y:
        # Move one along in the sequence so we can assume x > y.
        return find_in_sequence(y, y - x, n - 1)
    # Case when x > y.
    # We have blocks of (x, x - d, d, x - 2d, x - 3d, d, ...) until hit 0.
    d = x - y
    max_steps = x / d
    if max_steps % 2 == 0:
        # Need to end our blocks on d so if the last step before 0 is even then
        # we've gone too far so back up one block.
        max_steps -= 1
    # Add the contribution from the d terms to the limit of what we can get
    # from this part of the sequence.
    limit = max_steps + (max_steps + 1) / 2
    if n <= limit:
        # We can easily get the nth element. If n % 3 == 2 then it must be d
        # otherwise it is of the form x - a*d.
        return d if n % 3 == 2 else x - (2 * (n / 3) + n % 3) * d
    else:
        # Find it in the next generated sequence.
        return find_in_sequence(x - max_steps * d, d, n - limit + 1)


if __name__ == '__main__':
    print AbsSequence().getElements("0", "0", ["1000000000000000000"])
    print AbsSequence().getElements(710370, 177300, ["5","95","164721","418","3387","710","0","1197","19507","5848"])
