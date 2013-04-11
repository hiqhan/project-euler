#! /usr/bin/python2.7
import math


def getDivisors(n):
    u = int(math.sqrt(n))
    divisors = [1]
    for i in range(2, u):
        if n % i == 0:
            divisors.extend([i, n / i])

    if n % u == 0:
        divisors.append(u) if u * u == n else divisors.extend([u, n / u])

    return divisors


def getAbundantNums(n):
    abundantNums = [i for i in range(12, n) if sum(getDivisors(i)) > i]
    return abundantNums


if __name__ == '__main__':
    x = 28124
    res = getAbundantNums(x)
    members = range(x)

    for i in range(len(res)):
        for j in range(i, len(res)):
            idx = res[i] + res[j]
            if idx < x:
                members[idx] = 0

    print sum(members)
