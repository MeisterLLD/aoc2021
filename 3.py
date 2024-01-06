## Part 1
cols = list( zip(*open('3','r').read().splitlines()))

gamma = [ ]
for col in cols:
    gamma += [1] if sum( [x=='1' for x in col] ) >= len(col)/2 else [0]
epsilon = [1-x for x in gamma]

gamma = sum([ x*(2**i) for i,x in enumerate(reversed(gamma))   ])
epsilon = sum([ x*(2**i) for i,x in enumerate(reversed(epsilon))   ])

print('Part 1 :',gamma*epsilon)

## Part 2
numbers = open('3','r').read().splitlines()
numbers2 = numbers.copy()

pos = 0
while len(numbers) > 1:
    mostfreq = '1' if sum( [num[pos]=='1' for num in numbers] ) >= len(numbers)/2 else '0'
    numbers = [x for x in numbers if x[pos] == mostfreq]
    pos += 1
oxygen = sum([ int(x)*(2**i) for i,x in enumerate(reversed(numbers[0]))   ])

pos = 0
while len(numbers2) > 1:
    lessfreq = '0' if sum( [num[pos]=='0' for num in numbers2] ) <= len(numbers2)/2 else '1'
    numbers2 = [x for x in numbers2 if x[pos] == lessfreq]
    pos += 1
co2 = sum([ int(x)*(2**i) for i,x in enumerate(reversed(numbers2[0]))   ])

print('Part 2 :',oxygen*co2)