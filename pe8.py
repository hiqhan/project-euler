#! /usr/bin/env python2.7
#Purpose: This program solve the 8th problem at projectuler.net
#Input: 1000-digit numbers in data file
#Output: the greatest product of five consecutive digits in the 1000-digit numbers
import numpy


N = 5


def findgreatest(digits):
    ''' numpy.array(object) turn a list(object) into the array needed by numby
    ... then caculate the product of the array using prod()
    '''
    products = [(numpy.array(digits[i:i + 5])).prod() for i in range(len(digits))]
    maximum = max(products)

    return maximum


def getdigits(file1):
    global N
    with open(file1) as a_file:
        a_lines = a_file.readlines()
        a_lines = [a_lines[i].strip() for i in range(len(a_lines) - N)]
        a_string = ''.join(a_lines)
        a_list = [int(x) for x in list(a_string)]
        return a_list

if __name__ == '__main__':
    import sys
    input_file = sys.argv[1]
    numbers = getdigits(input_file)
    result = findgreatest(numbers)

    print('the maximum if {0}'.format(result))
