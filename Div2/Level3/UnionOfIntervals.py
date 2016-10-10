# Given a list of integers, find the n-th smallest number, i.e., the
# number that appears at index n (0-based) when they are sorted in
# non-descending order. The numbers will be given in intervals. For
# example, the intervals (1, 3) and (5, 7) represent the list of numbers {
# 1, 2, 3, 5, 6, 7 }. A number may be present in more than one interval,
# and it appears in the list once for each interval it is in. For example,
# the intervals (1, 4) and (3, 5) represent the list of numbers { 1, 2, 3,
# 3, 4, 4, 5 }.

# The intervals will be given as two int[]s, lowerBound and upperBound.
# The i-th elements of these int[]s represent the smallest and largest
# numbers in the i-th interval, inclusive.


class UnionOfIntervals(object):
    # Binary search for the nth element.
    def nthElement(self, lowerBound, upperBound, n):
        p = -2000000000
        r = 2000000000
        while p <= r:
            q = (p + r) / 2
            # lower_count represents the number of numbers less than q.
            # q_count represents the number of times q appears in the list.
            lower_count = 0
            q_count = 0
            for l_bound, u_bound in zip(lowerBound, upperBound):
                if q >= l_bound:
                    lower_count += min(q, u_bound + 1) - l_bound
                    if q <= u_bound:
                        q_count += 1
            if q_count > 0 and lower_count <= n < lower_count + q_count:
                return q
            elif n < lower_count:
                r = q - 1
            else:
                p = q + 1
        return None


if __name__ == '__main__':
    print UnionOfIntervals().nthElement([1, 5], [3, 7], 4)
