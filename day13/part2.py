file = "./example1.txt"
file = "./input1.txt"

with open(file) as f:
    machines = f.read().split("\n\n")
    for i, m in enumerate(machines):
        ba, bb, p = m.splitlines()

        coordsA = ba.split(":")[1].strip()
        coordsB = bb.split(":")[1].strip()
        coordsP = p.split(":")[1].strip()

        dxA, dyA = [int(c.split("+")[1]) for c in coordsA.split(",")]
        dxB, dyB = [int(c.split("+")[1]) for c in coordsB.split(",")]
        locX, locY = [int(c.split("=")[1]) for c in coordsP.split(",")]

        machines[i] = ((dxA, dyA), (dxB, dyB), (locX, locY))

    cost = 0
    for (dxA, dyA), (dxB, dyB), (locX, locY) in machines:
        locX, locY = locX + 10000000000000, locY + 10000000000000
        aHit = (locX * dyB - locY * dxB) / (dxA * dyB - dyA * dxB)
        bHit = (locX - aHit * dxA) / dxB

        if int(aHit) == aHit and int(bHit) == bHit:
            cost += 3 * aHit + bHit

    print(int(cost))