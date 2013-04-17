#! /usr/bin/python2.7


def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = a + b, a
        yield a


if __name__ == '__main__':
    gen = fib(pow(10, 999))
    nums = [n for n in gen]
    print len(nums)
