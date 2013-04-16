#! /usr/bin/python2.7
import itertools
import math


if __name__ == '__main__':
    #the following two commented line is a easy way to get the millionth permutation
    #perms = list(itertools.permutations(range(10)))
    #print ''.join(map(str, perms[999999]))

    #and i do some calculations first, figuring out that the millionth permutation must begins with '2'
    idx = 1000000 - math.factorial(9) * 2
    digits = range(10)
    digits.remove(2)
    perms = list(itertools.permutations(digits))
    print '2' + ''.join(map(str, perms[idx - 1]))
