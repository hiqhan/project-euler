#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set


# pe50_data contains primes below 1000000
with open('data/pe50_data', mode='r') as af:
    lines = af.readlines()
primes = [int(i.strip()) for i in lines]
pset = Set(primes)
l, u = len(primes), 1
while sum(primes[:u]) < primes[-1]:
    u += 1
#maxlen, p = 0, 0
#for step in range(22, u):
#    for idx in range(l - u):
#        tmp = sum(primes[idx:idx + step])
#        if tmp in pset and step > maxlen:
#            maxlen, p = step, tmp
#            print maxlen, p
#            break
#print maxlen, p


# trying the possibly largest step first, and stop finding when found one
# it gets the same result in the way trying with smallest step first.
maxlen, p, found = 0, 0, False
for step in range(u, 22, -1):
    for idx in range(l - u):
        tmp = sum(primes[idx:idx + step])
        if tmp in pset and step > maxlen:
            maxlen, p = step, tmp
            found = True
            break
    if found:
        break
print maxlen, p
