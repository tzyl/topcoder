import random


class SerialNumbers(object):
    def sortSerials(self, serialNumbers):
        serialNumbers = list(serialNumbers)
        quicksort(serialNumbers, key=self.compare_serials)
        return serialNumbers

    def compare_serials(self, s1, s2):
        """Returns -1 if s1 comes before s2 or 1 if s1 comes after s2."""
        if len(s1) != len(s2):
            return -1 if len(s1) < len(s2) else 1
        digit_sum1 = self.sum_digits(s1)
        digit_sum2 = self.sum_digits(s2)
        if digit_sum1 != digit_sum2:
            return -1 if digit_sum1 < digit_sum2 else 1
        return -1 if s1 < s2 else 1

    def sum_digits(self, s):
        return sum(int(c) for c in s if c in "0123456789")


def quicksort(A, key=cmp):
    def _quicksort(A, p, r):
        if p < r:
            q = partition(A, p, r, key)
            _quicksort(A, p, q - 1)
            _quicksort(A, q + 1, r)
    _quicksort(A, 0, len(A) - 1)


def partition(A, p, r, key):
    k = random.randint(p, r)
    A[r], A[k] = A[k], A[r]
    pivot = A[r]
    i = p - 1
    for j in xrange(p, r):
        if key(A[j], pivot) <= 0:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

if __name__ == '__main__':
    A = [5, 7, 3, 2, 7, 4, 1, 8]
    print A
    quicksort(A)
    print A
    serial_numbers = ["ABCD", "145C", "A", "A910", "Z321"]
    print SerialNumbers().sortSerials(serial_numbers)
