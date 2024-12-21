import sys
sys.path.insert(0, '..')

from utils import inBounds, DIRECTIONS
from collections import deque, defaultdict
from itertools import product


file = "./example1.txt"
file = "./input1.txt"

keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

dpad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

def getPaths(grid):
    paths = defaultdict(lambda: defaultdict(list))
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col is None: continue
            q = deque([(r, c, "")])
            seen = set()
            paths[col][col].append("A")
            while len(q):
                cr, cc, path = q.popleft()
                seen.add((cr, cc))
                for k, (dr, dc) in DIRECTIONS.items():
                    nr, nc = cr + dr, cc + dc
                    if not inBounds(grid, nr, nc): continue
                    if (nr, nc) in seen: continue
                    loc = grid[nr][nc]
                    if loc is None: continue
                    q.append((nr, nc, path + k))
                    paths[col][loc].append(path + k + "A")
    return paths

keypadPaths = getPaths(keypad)
dpadPaths = getPaths(dpad)

def findInputOptions(paths, code, currentPos):
    if code == "": return [""]
    loc = code[0]
    currentOptions = paths[currentPos][loc]
    nextOptions = findInputOptions(paths, code[1:], loc)

    combinations = ["".join(c) for c in product(currentOptions, nextOptions)]
    minLen = min(map(len, combinations))
    return list(filter(lambda c: len(c) == minLen, combinations))

with open(file) as f:
    codes = f.read().splitlines()

    res = 0
    for code in codes:

        options = findInputOptions(keypadPaths, code, "A")

        for _ in range(2):
            nextOptions = []
            for option in options:
                nextOptions += findInputOptions(dpadPaths, option, "A")
            minLen = min(map(len, nextOptions))
            options = list(filter(lambda o: len(o) == minLen, nextOptions))

        res += len(options[0]) * int(code[:-1])

    print(res)




