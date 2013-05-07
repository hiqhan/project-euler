#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def process(n):
    return sorted(str(n))


for n in range(10 ** 5, 10 ** 7):
    if (process(n) == process(2 * n) == process(3 * n) == process(4 * n) and
            process(n) == process(5 * n) == process(6 * n)):
        print n
        break
