#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import isPrime


def isTruncPrime(n):
    s = str(n)
    pre = ['1', '9']
    if s[0] in pre or s[-1] in pre:
        return False
    for i in range(1, len(s)):
        if not isPrime(int(s[:i])) or not isPrime(int(s[i:])):
            return False
    return True


def isPrimeWithOdd(n):
    even = ['0', '4', '6', '8']
    for i in even:
        if i in str(n):
            return False
    return True


primes = [i for i in range(11, pow(10, 6)) if isPrime(i) and isPrimeWithOdd(i)]
if __name__ == "__main__":
    res = [p for p in primes if isTruncPrime(p)]
    print sum(res)
