from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict


def flexradix(A, d):
    # Du mÃ¥ mest sannsynlig lage egne hjelpefunksjoner for denne funksjonen for Ã¥ lÃ¸se oppgaven.
    # Funksjonen skal returnere listen A sortert.
    # SKRIV DIN KODE HER


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