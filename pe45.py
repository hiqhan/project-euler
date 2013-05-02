#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set


def Tn():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1


def Pn():
    n = 1
    while True:
        yield n * (3 * n - 1) / 2
        n += 1


def Hn():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1


if __name__ == "__main__":
    limit, flag = 10000, False
    tn, pn, hn = Tn(), Pn(), Hn()
    ts, ps, hs = Set(), Set(), Set()
    while True:
        ts.union_update(Set([tn.next() for i in range(limit)]))
        ps.union_update(Set([pn.next() for i in range(limit)]))
        hs.union_update(Set([hn.next() for i in range(limit)]))
        for item in ts:
            if item in ps and item in hs:
                if item > 40755:
                    flag = True
                    print item
                    break
        if flag:
            break
