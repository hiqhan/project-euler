#! /usr/bin/python2.7
# -*- condig: utf-8 -*-
from common import isPrime


def Rotation(s):
    res = [s[i:] + s[:i] for i in range(len(s))]
    return res


def isCircularPrime(n):
    if '5' in str(n):
        return False

    if not isPrime(n):
        return False

    nums = Rotation(str(n))
    for n in nums[1:]:
        if not isPrime(int(n)):
            return False
    return True


if __name__ == "__main__":
    # i must be odd
    res = [i for i in range(11, pow(10, 6), 2) if isCircularPrime(i)]
    # don't forget to add the four circular primes below 10
    print 4 + len(res)
