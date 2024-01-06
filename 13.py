dots = set()
folds = [ ]
with open('13','r') as f:
    listofdots, listoffolds = f.read().split('\n\n')
    for instr in listofdots.splitlines():
        x, y = tuple(map(int,instr.split(',')))
        dots.add(  (x,y)  )
    for instr in listoffolds.splitlines():
        instr = instr.split('g ')[1]
        dir, val = instr.split('=')[0], int(instr.split('=')[1])
        folds.append( (dir,val)   )

## Part 1
def fold(dir, val, dots):
    if dir == 'x':
        tofold = set( (x,y) for (x,y) in dots if x > val )
        dots2 = set( (2*val - x,y) for (x,y) in tofold)
        return (dots | dots2) - tofold

    else:
        tofold = set( (x,y) for (x,y) in dots if y > val )
        dots2 = set( (x,2*val - y) for (x,y) in tofold)
        return (dots | dots2) - tofold

dir, val = folds.pop(0)
print('Part 1 :', len( dots:= fold(dir, val, dots)))

## Part 2
print('Part 2 :')
while folds:
    dir, val = folds.pop(0)
    dots = fold(dir, val, dots)

xmax = max(x for (x,y) in dots)
ymax = max(y for (x,y) in dots)

carte = [ ]
for y in range(ymax+1):
    ligne = ['# ' if (x,y) in dots else '  ' for x in range(xmax+1)]
    carte.append(ligne)

for ligne in carte:
    print(''.join(ligne))
