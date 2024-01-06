## Part 1
with open('4','r') as f:
    nums = list(map(int, f.readline().split(',')))
    f.readline()
    grids = []
    for grille in f.read().split('\n\n'):
        currentgrid = [ ]
        for row in grille.splitlines():
            currentgrid.append( list(map(int, [x for x in row.split(' ') if x != '']  ))     )
        grids.append(currentgrid)

ngrids = len(grids)
nlignes = len(grids[0])
ncols = len(grids[0][0])

found = False
delimiter = 0
while not found:
    delimiter += 1

    for grid in grids:
        for i in range(nlignes):
            if all( grid[i][j] in nums[0:delimiter] for j in range(ncols)    ):
                found = True
                break
        if found: break

        for j in range(ncols):
            if all( grid[i][j] in nums[0:delimiter] for i in range(nlignes)   ):
                found = True
                break
        if found: break

    winninggrid = grid
    winningnumber = nums[delimiter-1]


somme = 0
for i in range(nlignes):
    for j in range(ncols):
        if winninggrid[i][j] not in nums[0:delimiter]:
            somme += winninggrid[i][j]

print('Part 1 :', somme*winningnumber)

## Part 2
delimiters = [0]*ngrids
scores = [0]*ngrids

for N, grid in enumerate(grids):
    delimiter = delimiters[i]
    found = False

    while not found:
        delimiter += 1

        for i in range(nlignes):
            if all( grid[i][j] in nums[0:delimiter] for j in range(ncols)    ):
                found = True
                break

        if found: break

        for j in range(ncols):
            if all( grid[i][j] in nums[0:delimiter] for i in range(nlignes)   ):
                found = True
                break

        if found: break

    winningnumber = nums[delimiter-1]


    somme = 0
    for i in range(nlignes):
        for j in range(ncols):
            if grid[i][j] not in nums[0:delimiter]:
                somme += grid[i][j]

    scores[N] = somme*winningnumber
    delimiters[N] = delimiter

print('Part 2 :', scores[ delimiters.index(max(delimiters))  ]   )
