#from sys import stdin                                  #her må det endres før innlevering
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

def alph(char):
    return (ord(char) - 97)

def countingSort(start, end, A, r):
    counter = [0] * 26
    i = 0
    for i in range(start, (end + 1)):
        counter[alph(A[i][r])] += 1
    i = 0
    for i in range(26):
        counter[i] += counter[i - 1]

    B = [0] * (end - start + 1)
    i = 0
    for i in range(end, (start - 1), -1):
        B[counter[alph(A[i][r])] - 1] = A[i]
        counter[alph(A[i][r])] -= 1

    i = 0
    for i in range(end - start + 1):
        A[i + start] = B[i]

def countingsort( aList, k ):
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i] += 1

    ndx = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        aList[ndx] = i
        ndx += 1
        counter[i] -= 1

def insertionSort(A):
  for i in range(1, len(A)):
    tmp = A[i]
    k = i
    while k > 0 and tmp < A[k - 1]:
        A[k] = A[k - 1]
        k -= 1
    A[k] = tmp

def stringSort(start, end, arr, radix):
    arr = countingSort(start, end, arr, radix)
    x = start

    while arr[x][radix] == arr[x+1][radix]:
        x += 1
        end += 1
    countingSort(start, end, arr, radix+1)
    start = end+1

    if start == arr[end]:
        return arr


def flexradix(A, d):

    stringSort(0, (len(A) - 1), A, 0)

    return A

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