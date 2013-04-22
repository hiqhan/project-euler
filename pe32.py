#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set


def isPandigital(a, b):
    c = a * b
    s = str(a) + str(b) + str(c)
    if '0' in s or len(s) != 9 or len(Set(list(s))) != 9:
        return False
    return True


if __name__ == "__main__":
    a_arrs = [range(1, 10), range(10, 100)]
    b_arrs = [range(1000, 10000), range(100, 1000)]
    c = []

    for an, bn in zip(a_arrs, b_arrs):
        for a in an:
            for b in bn:
                if isPandigital(a, b):
                    c.append(a * b)

    print sum(Set(c))
