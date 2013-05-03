#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import isPrime
from sets import Set


def isConjecture(n):
    root = 1
    while 2 * pow(root, 2) <= n - 2:
        if n - 2 * pow(root, 2) in primes:
            return True
        root += 1
    return False


primes = Set([i for i in range(2, 10000) if isPrime(i)])
odds = Set(range(3, 10000, 2))
oddcomps = odds.difference(primes)
for n in oddcomps:
    if not isConjecture(n):
        print n
        break
