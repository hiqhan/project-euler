#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from sets import Set


# The key point in this solution is taking use of string comparison.Because it
# compare two string from the first character and return result once it finds
# different characters. For example, '9oc' > '9mc', '9g' > '8omn'. One string
# represent each 5-card case. For there are 9 situations in ranking ways, let
# the first character of each string vary from '9' to '1' and the following
# string also vary in different ways in each situation.
points = {'2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9,
          'T': 10,
          'J': 11,
          'Q': 12,
          'K': 13,
          'A': 14,
          }
# score is a string representing each 5-card case, like '9g', '8j' etc.
score = ''


def isStraightFlush(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    suits = [item[1] for item in cards]
    if len(Set(suits)) == 1 and len(Set(numbers)) == 5 and max(numbers) - min(numbers) == 4:
        score = '9' + chr(max(numbers) + ord('a'))
        return True
    else:
        return False


def isFourOfAKind(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    p = [0] * 15
    for n in numbers:
        p[n] += 1
    if len(Set(numbers)) == 2 and max(p) == 4:
        score = '8' + chr(p.index(4) + ord('a'))
        return True
    else:
        return False


def isFullHouse(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    p = [0] * 15
    for n in numbers:
        p[n] += 1
    if len(Set(numbers)) == 2 and max(p) == 3:
        score = '7' + chr(p.index(3) + ord('a'))
        return True
    else:
        return False


def isFlush(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    suits = [item[1] for item in cards]
    if len(Set(suits)) == 1:
        score = '6' + ''.join(chr(i + ord('a')) for i in sorted(numbers)[::-1])
        return True
    else:
        return False


def isStraight(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    if len(Set(numbers)) == 5 and max(numbers) - min(numbers) == 4:
        score = '5' + chr(max(numbers) + ord('a'))
        return True
    else:
        return False


def isThreeOfAKind(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    p = [0] * 15
    for n in numbers:
        p[n] += 1
    if max(p) == 3:
        score = '4' + chr(p.index(3) + ord('a'))
        return True
    else:
        return False


def isTwoPairs(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    p = [0] * 15
    for n in numbers:
        p[n] += 1
    if max(p) == 2 and len(Set(numbers)) == 3:
        a = p.index(2)
        b = 4 - p[::-1].index(2)
        m, n = max(a, b), min(a, b)
        score = '3' + chr(m + ord('a')) + chr(n + ord('a')) + chr(p.index(1) + ord('a'))
        return True
    else:
        return False


def isOnePair(cards):
    global score
    numbers = [points[item[0]] for item in cards]
    p = [0] * 15
    for n in numbers:
        p[n] += 1
    if max(p) == 2 and len(Set(numbers)) == 4:
        m = p.index(2)
        tmp = [n for n in p if p[n]]
        s = [chr(i + ord('a')) for i in sorted(tmp)[::-1]]
        score = '2' + chr(m + ord('a')) + ''.join(s)
        return True
    else:
        return False


def getHighCard(cards):
    global score
    numbers = sorted([points[item[0]] for item in cards])[::-1]
    score = '1' + ''.join([chr(i + ord('a')) for i in numbers])
    return score


def getScores(cards):
    global score
    res = 0
    if isStraightFlush(cards):
        res = score
    elif isFourOfAKind(cards):
        res = score
    elif isFullHouse(cards):
        res = score
    elif isFlush(cards):
        res = score
    elif isStraight(cards):
        res = score
    elif isThreeOfAKind(cards):
        res = score
    elif isTwoPairs(cards):
        res = score
    elif isOnePair(cards):
        res = score
    else:
        res = getHighCard(cards)
    return res


if __name__ == "__main__":
    with open('data/poker.txt', mode='r') as af:
        lines = af.readlines()
    count = 0
    for record in lines:
        s = record.split()
        cardsOfP1, cardsOfP2 = s[:5], s[5:]
        if getScores(cardsOfP1) > getScores(cardsOfP2):
            count += 1
    print count
