#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


n = range(1, 27)
s = [chr(ord('A') + i) for i in range(0, 26)]
chdict = dict(zip(s, n))

trinums = [int(n * (n + 1) / 2) for n in range(1, 20)]
tridict = dict(zip(trinums, [True] * len(trinums)))


def getNumofWord(word):
    num = 0
    for i in word:
        num += chdict[i]
    return num


if __name__ == "__main__":
    with open('data/words.txt', mode='r') as file_a:
        words = file_a.readline().split(",")
    total = 0
    for word in words:
        if getNumofWord(word.strip("\"")) in tridict:
            total += 1
    print total
