from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict


def flexradix(A, d):    # d = antall strenger
    # idé: hva med å dele opp strengene etter lengde for å samle de av lik lengde og merge sammen etterpå? Hmm, får kanskje kjøretid på Ø(n log n)...


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()