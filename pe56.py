#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def getSum(n, p):
    return sum([int(s) for s in str(n ** p)])


m, curn, curp = 0, 0, 0
for a in range(1, 100):
    for b in range(1, 100):
        tmp = getSum(a, b)
        if tmp > m:
            m, curn, curp = tmp, a, b

print m, curn, curp
