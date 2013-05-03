#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set
from common import isPrime


def findFirsNumber(arr, substring):
    s = ''.join([str(i) for i in arr])
    return s.find(substring)


def getAllPrimes(u):
    pdict = dict()
    allps = []
    for i in range(2, u):
        n, ps, flag = i,  [], True
        while n not in pset:
            if n in pdict:
                ps += pdict[n]
                flag = False
                break
            else:
                for p in primes:
                    if not n % p:
                        ps.append(p)
                        n /= p
                        break
        if flag:
            ps.append(n)
        allps.append(ps)
        pdict[i] = ps
    return allps


primes = [i for i in range(2, 1000000) if isPrime(i)]
pset = Set(primes)
distincts = [len(Set(ps)) for ps in getAllPrimes(1000000)]
print findFirsNumber(distincts, '4444') + 2
