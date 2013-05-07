#! /usr/bin/python2.7
# -*- coding: utf-8 -*
from math import factorial


count = 0
for n in range(1, 101):
    fn = factorial(n) / 1000000
    for r in range(n):
        if fn > factorial(r) * factorial(n - r):
            count += 2 * (n / 2 - r + 1)
            if 2 * (n / 2) == n:
                count -= 1
            break
print count
