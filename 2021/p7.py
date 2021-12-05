
deck = [0,0,-1,18,1,0,23,0,0,0,0,-1,0,0,-1,30,0,0,0,0,0,-1,7,0,0,0,12,39,0,-1,0,0,0,0,49,19,0,-1,53,0,24,0,0,0,0,42,0,0,32,0,-1,-1,0,0,0,-2]

results = []

def move(deck, moves, position, current, curMoves):
    # if position in current:
        # return
    current.append(position)
    if len(curMoves) > 14:
        return
    if position > len(deck):
        return
    for i in range(moves+1):
        if i == 0:
            continue
        newPos = position+i
        newCurMoves = curMoves[:]
        newCurMoves.append(i)
        if deck[newPos] == -1:
            moves += 1
        if deck[newPos] == -2:
            current.append(newPos)
            # print(current, newCurMoves)
            results.append(newCurMoves)
            return 
        if deck[newPos] > 0:
            newPos = deck[newPos]
        move(deck, moves, newPos, current[:], newCurMoves)


move(deck, 1, 0, [],[])

r = map(lambda x: (len(x), sum(x), x), results)


minLen = 1000000
minSum = 1000000
minPath = []

for v in r:
    # print(v[0],v[1],v[2])
    if minLen > v[0]:
        minLen = v[0]
        minSum = v[1]
        minPath = v[2]
    if minLen == v[0]:
        if minSum < v[1]:
            minPath = v[2]

print('\n')
print(minLen, minSum, minPath)
