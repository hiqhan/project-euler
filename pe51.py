#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set


# A prime can not be divided by 3 and the sum of digits in a number, which
# could be divided by 3 also can be divided by 3. So besides the digits to
# be replaced, the sum of the remaining digits couldn't be divided by 3.
# Actually we can figure out that in the eight prime family, the number of
# digits to be replaced should be times of 3 and the possible sum of the
# remaining digits.

# primes file contains primes below 1000000
with open('data/primes', mode='r') as af:
    lines = af.readlines()

primes = [int(i.strip()) for i in lines]
pset = Set(primes)


def findSum(u, n, partSum):
    """
    find the possible sum of the remaining digits that not be replaced.
    u is the upper limit of the sum, n represent n prime family and
    partSum is the sum of the digits to be replaced.
    """
    res = []
    for i in range(u):
        if i % 3:
            count = 1
            for p in partSum:
                if (i + p) % 3:
                    count += 1
            if count >= n:
                res.append(i)
    return res


def mlen(s):
    """
    figure out the most-seen digit in a number, this function return the
    digit and the repeated times.
    """
    count = [0] * 10
    for i in s:
        count[int(i)] += 1
    return (count.index(max(count)), max(count))


def isPDR(n, ch):
    s = str(n)
    count = 0
    for i in range(0, 10):
        curstr = s[:-1].replace(ch, str(i)) + s[-1]
        # the leading zero should not be considered
        if len(str(int(curstr))) == len(str(n)) and int(curstr) in pset:
            count += 1
    if count == 8:
        return True
    return False


for ds in range(3, 7, 3):
    # sum of digits to be replaced
    partSum = Set([i * ds for i in range(1, 10)])
    # sum of the remaining digits
    possibleSum = findSum(37, 8, partSum)
    done = False
    for n in primes:
        ml = mlen(str(n)[:-1])
        if ml[1] >= 3 and sum([int(s) for s in str(n).replace(str(ml[0]), '0')]) in possibleSum:
            if isPDR(n, str(ml[0])):
                print n
                done = True
                break
    if done:
        break
