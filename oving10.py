from sys import stdin

Inf = float('inf')


def mst(nm):
    mintre = prim(nm)
    summ = 0
    for (fra, til) in mintre:
        print('hei')
        summ = max(summ, nm[fra][til])
    return summ

def prim(nm):
    n = len(nm)
    tre = []
    bestenabo = [None] * n
    bestepris = [Inf] * n
    ikke_funnet = range(1, n)
    forrige = 0
    while len(ikke_funnet) > 0:
        for i in ikke_funnet:
            if nm[i][forrige] < bestepris[i]:
                bestenabo[i] = forrige
                bestepris[i] = nm[i][forrige]
        minpris = Inf
        for i in ikke_funnet:
            if bestepris[i] < minpris:
                nestefra = i
                nestetil = bestenabo[i]
                minpris = bestepris[i]
        tre.append( (nestefra,nestetil) )
        ikke_funnet.remove(nestefra)
        forrige = nestefra
    return tre

lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
print('bo')
neighbour_matrix = [None] * n
node = 0
for line in lines:
    neighbour_matrix[node] = [Inf] * n
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node][neighbour] = weight
    node += 1
print (mst(neighbour_matrix))