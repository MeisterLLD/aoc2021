from math import prod

carte = [ ]
with open('9','r') as f:
    for ligne in f.read().splitlines():
        carte.append( list(int(x) for x in ligne  ))

n = len(carte)
m = len(carte[0])


def voisins(pos):
    i, j = pos
    voisinspot = [(i-1,j), (i+1, j), (i,j-1), (i,j+1)]
    return [v for v in voisinspot if 0 <= v[0] < n and 0 <= v[1] < m]

## Part 1
lowest = [ ]
totalrisk = 0
for i in range(n):
    for j in range(m):
        if all( carte[i][j] < carte[v[0]][v[1]] for v in voisins((i,j))   ):
            totalrisk += carte[i][j] + 1
            lowest.append((i,j))

print('Part 1 :',totalrisk)

## Part 2
part2 = [ ]
for (i,j) in lowest:
    vus = set()
    pile = [(i,j)]
    while pile:
        pos = pile.pop()
        vus.add(pos)
        for v in voisins(pos):
            if v not in vus and carte[v[0]][v[1]] < 9:
                pile.append(v)

    part2.append(len(vus))

print('Part 2 :', prod(sorted(part2)[-3:]))