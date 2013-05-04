#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import isPrime


# let a, b, c be the increasing sequence, then a + c = 2 * b
# a, b, c all end with the same number like 1, 3, 7, 9
primes = [i for i in range(1000, 9999) if isPrime(i)]
pdict = dict()
pdict['1'], pdict['3'], pdict['7'], pdict['9'] = [], [], [], []
for p in primes:
    pdict[str(p)[-1]].append(p)


def findPP(arr):
    l = len(arr)
    for i in range(l):
        for j in range(i + 1, l):
            mid = (arr[i] + arr[j]) / 2
            if mid in arr and sorted(str(arr[i])) == sorted(str(mid)) == sorted(str(arr[j])):
                print str(arr[i]) + str(mid) + str(arr[j])


for k in pdict.keys():
    findPP(pdict[k])
