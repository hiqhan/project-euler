#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def rootConvergents():
    a, b = 1, 1
    while True:
        a, b = a + 2 * b, a + b
        yield a, b


if __name__ == "__main__":
    times, count = 1000, 0
    rc = rootConvergents()
    while times:
        a, b = rc.next()
        if len(str(a)) > len(str(b)):
            count += 1
        times -= 1
    print count
