L = [int(x) for x in open('1').read().splitlines()]
print('Part 1 :', sum(L[i+1] > L[i] for i in range(len(L)-1)  )  )
print('Part 2 :', sum(L[i+3] > L[i] for i in range(len(L)-3)  )  )