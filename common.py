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
