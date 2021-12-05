# https://interlos.fi.muni.cz/download/years/2021/sada2/connections.zip
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


    prevLen = 0
    iteration = 0
    while prevLen != len(connections):
        newCons = {}
        droppedCons = set()
        print("Iteration: ", iteration)
        iteration += 1
        prevLen = len(connections.keys())
        for i,v in connections.items():
            if len(v) >= 20 and len(v) < prevLen-20:
                newCons[i] = v
            else: 
                droppedCons.add(i)
        for i,v in newCons.items():
            newCons[i] = [k for k in v if k not in droppedCons]
        connections = newCons
        print(prevLen)

