from collections import defaultdict
G = defaultdict(list)
with open('12','r') as f:
    for ligne in f.read().splitlines():
        a, b = ligne.split('-')
        G[a].append(b)
        G[b].append(a)


## Part 1
def DFS(start, end, vus, path):
    if start == end:
        yield path

    for v in G[start]:
        if v not in vus:
            vus2 = vus.copy()
            if v.islower():  vus2.add(v)
            yield from DFS(v, end, vus2, path + [v])

N = len(list(DFS('start','end',{'start'},['start'])))
print('Part 1 :', N)

## Part 2
from time import time
def DFS2(start, end, vus, didtwice, path):
    if start == end:
        yield path

    for v in G[start]:
        if v not in vus:
            vus2 = vus.copy()
            if v.islower(): vus2.add(v)
            yield from DFS2(v, end, vus2, didtwice, path + [v])

        elif v in vus and not didtwice and v not in {'start','end'}:
            yield from DFS2(v, end, vus, True, path + [v])

N = len(list(DFS2('start','end',{'start'}, False, ['start'])))
print('Part 2 :', N)