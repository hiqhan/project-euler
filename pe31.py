#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


curUnits = [200, 100, 50, 20, 10, 5, 2]
nextUnits = [100, 50, 20, 10, 5, 2, 1]
units = dict(zip(curUnits, nextUnits))


def ways(n, curUnit):
    if curUnit == 1:
        return 1
    else:
        nextUnit = units[curUnit]
        res = sum([ways(n - i * curUnit, nextUnit) for i in range(n / curUnit + 1)])
        return res


if __name__ == "__main__":
    print ways(200, 200)
