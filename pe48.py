#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


#res = reduce(lambda x, y: x + y, map(lambda x: x ** x, range(1, 1001)))
res = sum([i ** i for i in range(1, 1001)])
print str(res)[-10:]
