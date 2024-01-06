rules = { }
with open('14','r') as f:
    init_polymer = f.readline().strip()
    f.readline()
    for ligne in f.read().splitlines():
        pair, res = ligne.split(' -> ')
        rules[pair] = res

def run(N):
    polymer = init_polymer
    counts = { x : polymer.count(x) for x in polymer }
    nbpairs = { }
    for i in range(len(polymer) - 1):
        g, d = polymer[i], polymer[i+1]
        nbpairs[g+d] = nbpairs.get(g+d, 0) + 1

    for _ in range(N):
        old_nbpairs = nbpairs.copy()
        for pair in old_nbpairs:
            new = rules[pair]
            counts[new] = counts.get(new, 0) + old_nbpairs[pair]       # on crée une nouvelle lettre plein de fois
            g, d = pair[0], pair[1]
            nbpairs[g+new] = nbpairs.get(g+new, 0) + old_nbpairs[pair] # on crée deux nouvelles
            nbpairs[new+d] = nbpairs.get(new+d, 0) + old_nbpairs[pair] # paires plein de fois
            nbpairs[g+d] -= old_nbpairs[pair]                          # mais on en casse d'autres !

    return max(counts.values())-min(counts.values())

## Part 1
print('Part 1 :', run(10))
## Part 2
print('Part 2 :', run(40))


