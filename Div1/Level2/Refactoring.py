def memoize(fn):
    cache = {}
    def wrapper(*args):
        key = args[1], args[2]
        if key not in cache:
            cache[key] = fn(*args)
        return cache[key]
    return wrapper


class Refactoring(object):
    def refactor(self, n):
        # primes = self.prime_sieve(2000000000)
        return self.refactor_helper(n, 2)

    @memoize
    def refactor_helper(self, n, min_):
        # if n in primes:
            # return 0
        total = 0
        i = min_
        while i * i <= n:
            if n % i == 0:
                total += 1
                total += self.refactor_helper(n / i, i)
            i += 1
        return total

    # def is_prime(self, n):
    #     if n <= 1:
    #         return False
    #     elif 2 <= n <= 3:
    #         return True
    #     i = 2
    #     while i * i <= n:

    # def refactor(self, n):
    #     p_factorization = self.prime_factorization(n)

    def prime_factorization(self, n):
        p_factorization = []
        primes = self.prime_sieve(n)
        for prime in primes:
            while n % prime == 0:
                p_factorization.append(prime)
                n /= prime
            if n == 1:
                break
        return p_factorization

    def prime_sieve(self, n):
        primes = set()
        A = [True] * (n + 1)
        A[0] = False
        A[1] = False
        for i, is_prime in enumerate(A):
            if is_prime:
                primes.add(i)
                for j in xrange(2*i, n + 1, i):
                    A[j] = False
        return primes

if __name__ == '__main__':
    print Refactoring().refactor(9240)
    print Refactoring().refactor(49)
    print Refactoring().refactor(1916006400)
    # print Refactoring().prime_factorization(2*2*2*3)
