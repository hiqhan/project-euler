#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set


def isPandigitalMulti(n):
    s, i = str(n), 2
    while True:
        s += str(n * i)
        if len(s) >= 9:
            break
        i += 1
    if len(s) == 9 and ''.join(sorted(Set(s))) == "123456789":
        return True
    return False


def GetPandigital(n):
    s, i = str(n), 2
    while True:
        s += str(n * i)
        if len(s) == 9:
            return s
        i += 1


if __name__ == "__main__":
    res = [i for i in range(9000, pow(10, 4)) if isPandigitalMulti(i)]
    pand = [GetPandigital(i) for i in res]
    print pand[-1]
