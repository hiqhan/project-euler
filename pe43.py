#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import itertools


def isSubStrDiv(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7, 0, -1):
        if int(str(n)[i:i + 3]) % primes[i - 1]:
            return False
    return True


if __name__ == "__main__":
    n = range(9, -1, -1)
    data = itertools.permutations(n)
    res = []
    for i in data:
        cur = int(''.join([str(item) for item in i]))
        if len(str(cur)) == 10 and isSubStrDiv(cur):
            res.append(cur)
    print sum(res)
