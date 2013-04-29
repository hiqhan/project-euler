#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import math


def isSqrtRoot(r, n):
    return r ** 2 == n


if __name__ == "__main__":
    res = [0] * 1001
    for a in range(2, 500):
        for b in range(1, a):
            c = int(math.sqrt(a ** 2 + b ** 2))
            if isSqrtRoot(c, a ** 2 + b ** 2):
                p = a + b + c
                if p <= 1000:
                    res[p] += 1

    print res.index(max(res))
