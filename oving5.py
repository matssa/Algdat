from sys import stdin

def alph(stri, r):
    if(not len(stri) > r):
        return 0
    return (ord(stri[r]) - 96)

def countingSort(start, end, A, r):
    counter = [0] * 27
    i = 0
    for i in range(start, (end + 1)):
        counter[alph(A[i], r)] += 1
    i = 0
    for i in range(1, 27):
        counter[i] += counter[i - 1]

    B = [0] * (end - start + 1)
    i = 0
    for i in range(end, (start - 1), -1):
        B[counter[alph(A[i], r)] - 1] = A[i]
        counter[alph(A[i], r)] -= 1

    i = 0
    for i in range(end - start + 1):
        A[i + start] = B[i]

def stringSort(start, end, arr, radix):
    countingSort(start, end, arr, radix)
    x = start
    y = start
    while y < end:
        while ((x < end) and ((len(arr[x]) <= radix) or (arr[x][radix] == arr[x+1][radix]))):
            if (len(arr[x]) <= radix):
                y += 1
            x += 1
        if (not (x == y)):
            stringSort(y, x, arr, radix + 1)
        x += 1
        y = x

def flexradix(A, d):
    stringSort(0, (len(A) - 1), A, 0)
    return A



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