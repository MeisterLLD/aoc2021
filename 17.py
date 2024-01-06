import re
from math import inf

with open('17','r') as f:
    xmin, xmax, ymin, ymax = tuple( map(int, re.findall(r"[-\d]+", f.readline())))

possible = set()
def getmaxheightfromlaunch(vx,vy):
    max = -inf
    x,y = 0,0
    while x <= xmax+1 and y >= ymin: # while reaching target is not excluded
        x += vx
        y += vy

        if y > max:
            max = y

        vx -= 1 if vx > 0 else -1 if vx < 0 else 0
        vy -= 1

        if xmin<=x<=xmax and ymin<=y<=ymax: # successful launch
            return max

    return -inf # unsuccessful launch

max = -inf
for vx in range(0,xmax+1):
    for vy in range(-abs(ymin), abs(ymin)+1):

        '''Explanation of this range :
        • the starting value is quite clear : below that we directly miss the target
        • for the ending value : once the bullet reaches y=0 again, it will have the
        same y-velocity in absolute value as when launched. Thus if this initial velocity
        is > abs(ymin), it is just like above '''

        new = getmaxheightfromlaunch(vx,vy)
        if new != -inf:
            possible.add((vx,vy))
        if new > max:
            max = new

print('Part 1 :', max)
print('Part 2 :', len(possible))
