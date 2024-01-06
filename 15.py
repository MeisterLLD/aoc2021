from heapq import heappop, heappush
from math import inf

carte = [ ]
with open('15','r') as f:
    for ligne in f.read().splitlines():
        carte.append([int(x) for x in ligne])

def voisins(carte, pos):
    n, m = len(carte), len(carte[0])
    i, j = pos
    voisinspot = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    return [ ((i,j), carte[i][j]) for (i,j) in voisinspot if 0<=i<n and 0<=j<m]

def dijkstra(carte, debut):
    n, m = len(carte), len(carte[0])
    q = [ (0,  debut)   ]
    dists = {debut : 0}

    while len(q) > 0:
        dist, pos = heappop(q)
        i, j = pos
        if i == n-1 and j == m-1:
            return dist

        for (v, cost) in voisins(carte, pos):
            if dist + cost < dists.get(v, inf):
                dists[v] = dist + cost
                heappush(q, (dist + cost, v) )

## Part 1
print('Part 1 :', dijkstra(carte, (0,0)))

## Part 2
from copy import deepcopy
n, m = len(carte), len(carte[0])

for _ in range(4): # Extend rows
    carte2 = deepcopy(carte[-n::])
    for i in range(n):
        for j in range(m):
            carte2[i][j] = carte2[i][j] + 1 if carte2[i][j] < 9 else 1
    carte = carte + carte2

for _ in range(4): # Extend cols
    for i, ligne in enumerate(carte):
        ligne2 = deepcopy(ligne[-m::])
        for j in range(m):
            ligne2[j] = ligne2[j] + 1 if ligne2[j] < 9 else 1
        carte[i] = ligne + ligne2

print('Part 2 :', dijkstra(carte, (0,0)))
