#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def buildTree(node, word):
    letter = word[0]
    word = word[1:]
    if not letter in node.barn:
        node.barn[letter] = Node()
    if not word:
        return node.barn[letter]
    return buildTree(node.barn[letter], word)

def bygg(ordliste):
    toppNode = Node()
    for tuppel in ordliste:
        endNode = buildTree(toppNode, tuppel[0])
        endNode.posi.append(tuppel[1])
    return toppNode

def posisjoner(ord, indeks, node):
    pos = []
    for letter in ord:
        pos.sort()
        if letter in node.barn:
            node = node.barn[letter]
            indeks += 1
            if indeks == len(ord):
                for i in node.posi:
                    pos.append(i)
                return pos
        elif letter == '?':
            indeks += 1
            if indeks == len(ord):
                for b in node.barn:
                    barnet = node.barn[b]
                    for i in barnet.posi:
                        pos.append(i)
                return pos
            for i in node.barn:
                index = indeks
                barnet = node.barn[i]
                if ord[index] in barnet.barn:
                    while index != len(ord):
                        barnet = barnet.barn[ord[index]]
                        index += 1
                    for p in barnet.posi:
                            pos.append(p)
                if pos:
                    return pos
    return pos

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()