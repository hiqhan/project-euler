#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import isPrime


def quadratic(a, b):
    """
    If n^2 + a*n + b is a quadratic formula then return the number of prime
    it produces, else return 0
    """
    n = 1
    while True:
        fn = n * (n + a) + b
        if not isPrime(fn):
            break
        else:
            n += 1

    return n - 1

if __name__ == "__main__":
    nums, product = -1, 0
    primes = [n for n in range(2, 1000) if isPrime(n)]
    # derivation of f(n)=n^2+a*n+b is f'=2*n+a, so f(n) get its minimum value when
    # n=-a/2, and f(-a/2)=b-(a^2)/4 must be greater than 2(the smallest prime)
    # when a is lesser than zero.
    # For b is up to 999,so we get 4*999-8 >= a^2, then a >= -63 when a is
    # negative, so a starts at -63
    for a in range(-63, 1000):
        # b must prime because f(n) = b (when n=0)
        for b in primes:
            if a == 0 or (a < 0 and 4 * b - a ** 2 - 8 < 0):
                continue
            tmp = quadratic(a, b)
            if nums < tmp:
                nums = tmp
                product = a * b

    print product
