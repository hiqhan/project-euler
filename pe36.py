#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def isPalindroms(n):
    binstr = bin(n)[2:]
    return str(n) == str(n)[::-1] and binstr == binstr[::-1]


print sum([i for i in range(pow(10, 6)) if isPalindroms(i)])
