#! /usr/bin/python2.7


def digitsOfRc(d):
    """
    get digits of recurring cycle of 1/d
    digitsOfRc(7) returns 6 because 1/7 = 0.(142857)
    """
    #if remainder occurred before, then it begins recurring cycle
    #so we get the digits
    n, visited = 1, []
    while True:
        visited.append(n)
        remainder = (n * 10) % d
        if not remainder:
            return 0
        elif remainder in visited:
            return len(visited) - visited.index(remainder)
        else:
            n = remainder


if __name__ == '__main__':
    digits = [digitsOfRc(num) for num in range(1, 1000)]
    print digits.index(max(digits)) + 1
