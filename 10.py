## Part 1
chartoscore = {')':3,  ']':57,  '}':1197,  '>':25137}
openers = '([{<'
closers = ')]}>'
opentoclose ={'(':')',  '[':']',  '{':'}',  '<':'>'}

score = 0
lines = [ ]

with open('10','r') as f:
    for ligne in f.read().splitlines():
        pile = [ ]
        for x in ligne:
            if x in openers:
                pile.append(x)

            if x in closers:
                y = pile.pop()
                if x != opentoclose[y]:
                    score += chartoscore[x]
                    break
        else:
            lines.append(ligne)

print('Part 1 :',score)

## Part 2
chartoscore = {')':1,  ']':2,  '}':3,  '>':4}

scores = [ ]

for ligne in lines:
    score = 0
    pile = [ ]
    for x in ligne:
        if x in openers:
            pile.append(x)
        if x in closers:
            pile.pop()

    for opener in pile[::-1]:
        score = 5*score + chartoscore[opentoclose[opener]]

    scores.append(score)

print('Part 2 :', sorted(scores)[len(scores)//2])