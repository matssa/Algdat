#!/usr/bin/python3

stdin = ["i:1,3,5,8", "n:2", "t:4,7", "a:6", "v:9"]
#from sys import stdin
from itertools import repeat
import math


def merge(decks):
    length = math.ceil(len(decks)/2)

    print(decks)


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()

