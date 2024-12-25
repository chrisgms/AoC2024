file = "./example1.txt"
file = "./input1.txt"

def getLockHeight(lock):
    heights = [0] * 5
    for c in range(5):
        for r in range(1, len(lock)):
            if lock[r][c] == ".": break
            heights[c] += 1
    return heights

def getKeyHeight(lock):
    heights = [0] * 5
    for c in range(5):
        for r in range(len(lock) - 2, 0, -1):
            if lock[r][c] == ".": break
            heights[c] += 1
    return heights


with open(file) as f:
    keyLocks = [kl.splitlines() for kl in f.read().split("\n\n")]

    keys = []
    locks = []

    for kl in keyLocks:
        if kl[0][0] == "#": locks.append(getLockHeight(kl))
        else: keys.append(getKeyHeight(kl))


    count = 0
    for l in locks:
        for k in keys:
            cols = list(map(sum, zip(k, l)))
            if all(map(lambda c: c <= 5, cols)): count += 1
    
    print(count)
