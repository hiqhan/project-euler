#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import math


def isPrime(n):
    if not isinstance(n, int):
        raise ValueError("n must be int")
    elif n < 2:
        raise ValueError("n must be greater than 1")
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if not n % i:
                return False

    return True


def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a, b must be ints")
    a, b = max(abs(a), abs(b)), min(abs(a), abs(b))
    while a % b:
        a, b = b, a % b

    return b
