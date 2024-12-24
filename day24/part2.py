import networkx as nx

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

    swaps = [
        ("z11", "rpv"),
        ("rpb", "ctg"),
        ("z31", "dmh"),
        ("z38", "dvq"),
    ]

    for w1, w2 in swaps:
        gates[w1], gates[w2] = gates[w2], gates[w1]
    
    G = nx.DiGraph()
    for w3, (w1, op, w2) in gates.items():
        G.add_edge(w1, w3, label=op)
        G.add_edge(w2, w3, label=op)
    
    with open("dot.txt", "w") as f2:
        dot = nx.drawing.nx_pydot.to_pydot(G)
        f2.write(dot.to_string())


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
    
    xGates = list(filter(lambda w: w[0].startswith("x"), wires.items()))
    yGates = list(filter(lambda w: w[0].startswith("y"), wires.items()))
    zGates = list(filter(lambda w: w[0].startswith("z"), wires.items()))
    
    xGates.sort(reverse=1)
    yGates.sort(reverse=1)
    zGates.sort(reverse=1)
    
    xBinary = "".join([str(s) for _, s in xGates])
    yBinary = "".join([str(s) for _, s in yGates])
    zBinary = "".join([str(s) for _, s in zGates])
    
    xDecimal = int(xBinary, base=2)
    yDecimal = int(yBinary, base=2)
    zDecimal = int(zBinary, base=2)

    zDecExpected = xDecimal + yDecimal
    zBinExpected = "{0:b}".format(zDecExpected)

    zBinDiffed = []
    zBinExpectedDiffed = []
    diffIdx = []
    for i in range(len(zBinary)):
        z1 = zBinary[i]
        z2 = zBinExpected[i]
        if z1 == z2:
            zBinDiffed.append(z1)
            zBinExpectedDiffed.append(z2)
        else:
            diffIdx.append(i)
            zBinDiffed += ["_", z1, "_"]
            zBinExpectedDiffed += ["_", z2, "_"]

    zBinaryDiff = "".join(zBinDiffed)
    zBinExpectedDiff = "".join(zBinExpectedDiffed)
    
    # print("x:")
    # print(xBinary)
    # print(xDecimal)
    # print("\ny:")
    # print(yBinary)
    # print(yDecimal)
    print("z (actual):")
    print(zBinary)
    print(zDecimal)
    print("\nz (expected):")
    print(zBinExpected)
    print(zDecExpected)
    if len(diffIdx):
        print("\nDiffs")
        print(zBinaryDiff)
        print(zBinExpectedDiff)
        print(f"\nMismatch at {len(zBinary) - diffIdx[-1] - 1}")
    else:
        print("\nMatched!")
        swapped = [w for ws in swaps for w in ws]
        print(",".join(sorted(swapped)))

    
    

    