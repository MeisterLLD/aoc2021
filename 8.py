## Part 1
signals, outputs = [ ], [ ]
with open('8','r') as f:
    for ligne in f.read().splitlines():
        signals.append(ligne.split(' | ')[0])
        outputs.append(ligne.split(' | ')[1])

count = 0
for output in outputs:
    for word in output.split(' '):
        if len(word) in {2,3,4,7}:
            count += 1

print('Part 1 :',count)

## Part 2
zero, one, two, three, four, five, six, seven, eight, nine = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()

total = 0
for i, signal in enumerate(signals):
    for sig in sorted(signal.split(' '), key = len):
        if len(sig) == 2: one = set(sig)
        if len(sig) == 3: seven = set(sig)
        if len(sig) == 4: four = set(sig)
        if len(sig) == 5:
            if len(set(sig) & one) == 2: three = set(sig)
            elif len(set(sig) & four) == 3:  five = set(sig)
            else: two = set(sig)
        if len(sig) == 6:
            if len(set(sig) & one) == 1: six = set(sig)
            elif len(set(sig) & four) == 4: nine = set(sig)
            else: zero = set(sig)
        else:
            eight = set(sig)

    settocypher = {tuple(sorted(zero)):'0', tuple(sorted(one)):'1', tuple(sorted(two)):'2', tuple(sorted(three)):'3', tuple(sorted(four)):'4', tuple(sorted(five)):'5', tuple(sorted(six)):'6', tuple(sorted(seven)):'7', tuple(sorted(eight)):'8', tuple(sorted(nine)):'9'}

    out = ''.join(  [settocypher[tuple(sorted(set(output)))] for output in outputs[i].split(' ')]  )
    total += int(out)

print('Part 2 :',total)