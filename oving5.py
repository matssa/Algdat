#from sys import stdin                                  #her må det endres før innlevering
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict



def flexradix(A, d):    # d = lengden på den lengste strengen
    # idé: hva med å dele opp strengene etter lengde for å samle de av lik lengde og merge sammen etterpå? Hmm, får kanskje kjøretid på Ø(n log n)...
    return A # tull

def main():
    stdin = open('eksInput.txt', 'r')           #Her kommer eksempelkoden inn i bildet. NB: fjern denne linja når ferdig!
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()