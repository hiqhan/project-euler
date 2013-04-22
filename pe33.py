#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set
from common import gcd


def isCuriousFact(a, b):
    sa, sb = str(a), str(b)
    if a == b or '0' in sa + sb:
        return False
    elif len(Set(sa + sb)) != 3:
        return False
    elif sa[0] == sa[1] or sb[0] == sb[1]:
        return False
    else:
        cancelNum = sa[0] if sa[0] in sb else sa[1]
        newSa = sa.replace(cancelNum, "")
        newSb = sb.replace(cancelNum, "")
        if a * int(newSb) != b * int(newSa):
            return False
        return True


if __name__ == "__main__":
    c = []
    for a in range(10, 51):
        for b in range(51, 100):
            if isCuriousFact(a, b):
                c.append((a, b))

    prod = lambda x, y: x * y
    numerator = reduce(prod, [item[0] for item in c])
    denominator = reduce(prod, [item[1] for item in c])
    print denominator / gcd(numerator, denominator)
