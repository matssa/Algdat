from sys import stdin
Inf = float('inf')

def mst(nm):
    mintre = prim(nm)
    sum = 0
    for (fra, til) in mintre:
        sum = max(sum, nm[fra][til])
    return sum

def prim(nm):
    tre = []
    bestenabo = [None] * len(nm)
    bestepris = [Inf] * len(nm)
    ikke_funnet = list(range(1, len(nm)))
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
        tre.append((nestefra, nestetil))
        ikke_funnet.remove(nestefra)
        forrige = nestefra
    return tre

lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
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