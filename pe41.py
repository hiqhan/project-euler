#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import isPrime
import itertools


# sum(range(1,10)) = 45, which can be divided by 3, so 9-bit number is impossible
# so does 8-bit numbers, while 7-bit numbers might be fit
# starting from the largest 7-bit number, so it doesn't need to check the
# maximum
nums = itertools.permutations(range(7, 0, -1))
for i in nums:
    cur = int(''.join([str(item) for item in i]))
    if isPrime(cur):
        print cur
        break
