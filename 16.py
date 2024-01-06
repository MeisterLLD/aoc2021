with open('16','r') as f:
    input = ''.join(  bin(int(x, 16))[2:].zfill(4) for x in  f.read().strip()  )

## Part 1
def sumv(input):
    if set(input) == {'0'} or input == '':
        return 0 # cas de base

    # On parse le premier paquet
    i = 0
    version = int(input[i: (i:= i+3)], 2)
    type = int(input[i: (i:= i+3)], 2)

    if type == 4: # literal, CAS DE BASE
        j = i # trouver le nombre de blocs
        while input[j] != '0':
            j += 5
        j = j+5

        blocks = [ input[i+5*k:i+5*(k+1)][1:] for k in range((j-i)//5)   ] # trouver les blocks
        literalvalue = int(''.join(blocks), 2)

        return version + sumv(input[j:]) # on parse la suite

    else: # operation packet
        lengthtypeid = int(input[i])
        i += 1
        if lengthtypeid == 0:
            length = int(input[i: (i:=i+15)  ], 2) # lenth useless here but i += 15 is needed
            return version + sumv( input[i:  ])
        else:
            numberofsubpackets = int(input[i: (i:=i+11)  ], 2) # useless except i += 11
            return version + sumv(input[i: ])

print('Part 1 :', sumv(input))

## Part 2
from math import prod

def operation(type, L):
    match type:
        case 0: return sum(L)
        case 1: return prod(L)
        case 2: return min(L)
        case 3: return max(L)
        case 5: return int(L[0] > L[1])
        case 6: return int(L[0] < L[1])
        case 7: return int(L[0] == L[1])

def evaluate(input):
    if set(input) == {'0'} or input=='': return 0

    i = 0
    version = int(input[i: (i:= i+3)], 2)
    type = int(input[i: (i:= i+3)], 2)

    if type == 4:  # LITERAL
        j = i
        while input[j] != '0':
            j += 5
        j = j+5
        blocks = [ input[i+5*k:i+5*(k+1)][1:] for k in range((j-i)//5)   ]
        literalvalue = int(''.join(blocks), 2)
        return (i:=j), literalvalue  # return the current index and the value of literal


    else: # OPERATION
        lengthtypeid = int(input[i])
        i += 1
        L = [ ]

        if lengthtypeid == 0:
            length = int(input[i: (i:=i+15)  ], 2)
            fin = i + length
            while i < fin:
                shift, subpacket = evaluate( input[i:]  )
                i += shift
                L.append(subpacket)

        else:
            numberofsubpackets = int(input[i: (i:=i+11)  ], 2)
            for _ in range(numberofsubpackets):
                shift, subpacket = evaluate( input[i:]  )
                i += shift
                L.append(subpacket)

    return i, operation(type, L) # return the current index and the result of operation in the packet

print('Part 2 :',evaluate(input)[1])