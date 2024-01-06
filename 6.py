with open("6", 'r') as f:
    init_fish = list(map(int, f.read().split(",")))

def totalfish(ndays):
    fish = [init_fish.count(i) for i in range(9)]
    for _ in range(ndays):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
    return sum(fish)

print('Part 1 :', totalfish(80))
print('Part 2 :', totalfish(256))