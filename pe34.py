#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import math


facts = [math.factorial(i) for i in range(10)]


def isDigitFact(n):
    res = sum(facts[int(s)] for s in str(n))
    return res == n


if __name__ == "__main__":
    print sum([n for n in range(100, facts[9] * 10) if isDigitFact(n)])
