d=[(abs(x//41%2*39-x%41),abs(y//7%2
*5-y%7))for x,y in[map(int,p.split
(','))for p in open('13')if','in p]]
for y in range(6):print(*[' #'[
(x,y)in d]for x in range(40)])