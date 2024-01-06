from copy import deepcopy
carte = [ ]
with open('11','r') as f:
    for ligne in f.read().splitlines():
        carte.append(   [int(x) for x in ligne]   )

oldcarte = deepcopy(carte)
n, m = len(carte), len(carte[0])

## Part 1
def voisins(pos):
    i, j = pos
    voisinspot = [ (i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)    ]
    return [(i,j) for (i,j) in voisinspot if 0 <= i < n and 0 <= j < m]


def flash(pos, carte, flashed):
    if pos in flashed:
        return None
    flashed.add(pos)

    for i,j in voisins(pos):
        carte[i][j] += 1
        if carte[i][j] > 9:
            flash((i,j), carte, flashed)

flashes = 0
for _ in range(100):
    flashed = set()
    for i in range(n):
        for j in range(m):
            carte[i][j] += 1

    toflash = [(i,j) for i in range(n) for j in range(m) if carte[i][j] > 9]

    for (i,j) in toflash:
        flash((i,j), carte, flashed)

    for (i,j) in flashed:
        carte[i][j] = 0
        flashes += 1

print('Part 1 :',flashes)

## Part 2
carte = oldcarte

def synchro():
    N = 0
    while True:
        N += 1
        this_turn_flashes = 0

        for i in range(n):
            for j in range(m):
                carte[i][j] += 1
        toflash = [(i,j) for i in range(n) for j in range(m) if carte[i][j] > 9]
        flashed = set()

        for (i,j) in toflash:
            flash((i,j), carte, flashed)

        for (i,j) in flashed:
            carte[i][j] = 0
            this_turn_flashes += 1
            if this_turn_flashes == n*m:
                return N

print('Part 2 :',synchro())