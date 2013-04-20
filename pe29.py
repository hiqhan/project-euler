#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set

res = [pow(a, b) for a in range(2, 101) for b in range(2, 101)]
print len(Set(res))
