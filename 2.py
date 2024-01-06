x, depth = 0, 0
with open('2','r') as f:
    for ligne in f.read().splitlines():
        dir, num = ligne.split(' ')
        num = int(num)
        if dir == 'forward':
            x += num
        else:
            depth += num if dir == 'down' else -num

print('Part 1 :', x*depth)

## Part 2
x, depth, aim = 0, 0, 0
with open('2','r') as f:
    for ligne in f.read().splitlines():
        dir, num = ligne.split(' ')
        num = int(num)
        if dir == 'down':
            aim += num
        if dir == 'up':
            aim -= num
        if dir == 'forward':
            x += num
            depth += aim*num

print('Part 2 :', x*depth)