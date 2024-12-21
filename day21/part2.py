import sys
sys.path.insert(0, '..')

from utils import inBounds, DIRECTIONS
from collections import deque, defaultdict
from itertools import product
from functools import cache


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

@cache
def dfs(start, end, depth):
    possiblePaths = dpadPaths[start][end]
    if depth == 1: return len(possiblePaths[0])

    minLen = float("inf")
    for p in possiblePaths:
        pLen = 0
        p = "A" + p
        for (s, e) in zip(p, p[1:]):
            pLen += dfs(s, e, depth - 1)
        minLen = min(minLen, pLen)
    return minLen
    
with open(file) as f:
    codes = f.read().splitlines()

    res = 0
    for code in codes:
        options = findInputOptions(keypadPaths, code, "A")
        minLen = float("inf")
        for option in options:
            oLen = 0
            option = "A" + option
            for (s, e) in zip(option, option[1:]):
                oLen += dfs(s, e, 25)
            minLen = min(minLen, oLen)

        res += minLen * int(code[:-1])

    print(res)




