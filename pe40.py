#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


# I did it by hand. This problem is same to calculating the number of digit a
# book used with n pages.For different n, it has different formula
# [1, 9], f(n) = n
# [10, 99], f(n) = (n-9)*2 + 9
# [100, 999], f(n) = (n-99)*3 + (99-9)*2 + 9 = (n-99)*3 + 189
# [1000, 9999], f(n) = (n-999)*4 + 2889
# [10000, 99999], f(n) = (n-9999)*5 + 3889
# [100000, 999999], f(n) = (n-99999)*6 + 48889
# ......
# but please note that you must calculate which digit of n is dx(x=1,10,100,..)
# after figuring out the number n.
# the numbers are: 1,10,55,370,2777,22222,185185
# but the correct digits for each number are:1,1,5,3,7,2,1,then we get 210.
