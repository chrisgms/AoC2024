file = "./example1.txt"
file = "./input1.txt"

with open(file) as f:
    initialStates, gateConns = f.read().split("\n\n")

    wires = {}

    for w, s in [l.split(": ") for l in initialStates.splitlines()]:
        wires[w] = int(s)

    gates = {}
    gateCount = 0
    for w1, op, w2, _, w3 in [l.split(" ") for l in gateConns.splitlines()]:
        gates[w3] = (w1, op, w2)
        wires[w3] = None
        gateCount += 1

    while gateCount > 0:
        for w, s in wires.items():
            if s is not None: continue

            w1, op, w2 = gates[w]
            s1, s2 = wires[w1], wires[w2]

            if s1 is None or s2 is None: continue

            if op == "AND": wires[w] = s1 and s2
            elif op == "OR": wires[w] = s1 or s2
            else: wires[w] = s1 ^ s2

            gateCount -= 1
    
    zGates = list(filter(lambda w: w[0].startswith("z"), wires.items()))
    zGates.sort(reverse=1)
    binary = "".join([str(s) for _, s in zGates])
    print(int(binary, base=2))

    
    

    