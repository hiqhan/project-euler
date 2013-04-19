#! /usr/bin/python2.7
# -*-: coding: utf-8 -*-


def sumOfSeq(a, d, n):
    """
    Return sum of arithmetic progression with n elements
    """
    return a * n + n * (n - 1) * d / 2


def sumOfNumsOnDiag(n):
    odds = xrange(3, n + 1, 2)
    # lrn: array of the lower right numbers in all nxn spirals
    lrn = [(i - 2) ** 2 + i - 1 for i in odds]
    # dis: array of distances betweeen lower right number and lower left number in all nxn spirals
    dis = [i - 1 for i in odds]
    res = 1 + sum(sumOfSeq(a, d, 4) for a, d in zip(lrn, dis))

    return res


if __name__ == "__main__":
    n = 1001
    print sumOfNumsOnDiag(n)
    # In fact, lrn and dis are variables dependent on i which is odd number
    # from 3 to 1001, so we can put them in one formula
    # get the result with the following one line command
    #print 1 + sum(4 * ((i - 2) ** 2) + 10 * (i - 1) for i in xrange(3, 1002, 2))
