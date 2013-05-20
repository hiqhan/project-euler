#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def isLychrel(n):
    times = 50
    while times:
        n = n + int(str(n)[::-1])
        if n == int(str(n)[::-1]):
            return False
        times -= 1
    return True


if __name__ == "__main__":
    res = [1 for i in range(1, 10001) if isLychrel(i)]
    print sum(res)
