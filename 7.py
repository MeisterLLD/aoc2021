poss = list(map(int,open('7','r').read().split(',')))
cost = 0

while len(set(poss)) > 1:
    med = sorted(poss)[len(poss)//2]
    for i, x in enumerate(poss):
        if x < med:
            poss[i] = x+1
            cost += 1
        if x > med:
            poss[i] = x-1
            cost += 1

print('Part 1 :',cost)

## Part 2
poss = list(map(int,open('7','r').read().split(',')))

def cost(poss, target):
    c = 0
    for x in poss:
        d = abs(target-x)
        c += d*(d+1)/2

    return c


m, M = min(poss), max(poss)
from math import inf
c = inf
for target in range(m, M+1):
    newc = cost( poss, target )
    if newc < c:
        c = newc

print('Part 2 :',c)
