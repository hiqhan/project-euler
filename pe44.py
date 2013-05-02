#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set


def getMiniumDis(arr):
    # let f(n) be n*(3*n - 1)/2, assuming that f(k), f(j) is what we find.
    # f(k) - f(j) = f(i) -> f(i) + f(j) = f(k)
    # f(k) + f(j) = f(i) + 2*f(j) = f(m)
    # so if both f(i) + f(j) and f(i) + 2*f(j) are pantagon numbers, then the
    # smallest f(i), namely f(k) - f(j) is what we want to find.
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] in pantset and arr[i] + 2 * arr[j] in pantset:
                return arr[i]


pantagons = [n * (3 * n - 1) / 2 for n in range(1, 3001)]
pantset = Set(pantagons)
print getMiniumDis(pantagons)
