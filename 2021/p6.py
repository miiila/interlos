
with open('connections.txt') as f:
    lines = f.readlines()
    connections = {}
    
    amount = 0

    for line in lines:
        fr, to = line.strip().split(' - ')
        fr = int(fr)
        to = int(to)
        if fr not in connections:
            connections[fr] = []
        if to not in connections:
            connections[to] = []
        connections[fr].append(to)
        connections[to].append(fr)


    newCons = {}
    prevLen = 0
    iteration = 0
    droppedCons = []
    while prevLen != len(connections):
        print(iteration)
        iteration += 1
        prevLen = len(connections.keys())
        for i,v in connections.items():
            if len(v) >= 20:
                newCons[i] = v
            else: 
                droppedCons.append(i)
        for i,v in newCons.items():
            newCons[i] = [k for k in v if k not in droppedCons]
        connections = newCons

