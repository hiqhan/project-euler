#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def s(n):
    res = 0
    while n:
        # p5 is a array contains 0^5, 1^5, ..., 9^5
        res += p5[n % 10]
        n /= 10
    return res


p5 = [n ** 5 for n in range(10)]
nums = [i for i in range(2, pow(9, 5) * 6) if s(i) == i]
print sum(nums)
