from heapq import heappop, heappush
from collections import defaultdict

file = "./example1.txt"
file = "./input1.txt"

width = 70
height = 70
bytes = 1024

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

def manhattanD(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return abs(r2 - r1) + abs(c2 - c1)

with open(file) as f:
    grid = [["." for _ in range(width + 1)] for _ in range(height + 1)]

    for c, r in [map(int, l.split(",")) for l in f.read().splitlines()][:bytes]:
        grid[r][c] = "#"

    start = (0, 0)
    end = (height, width)

    seen = set()
    bestHeuristic = defaultdict(lambda: float("inf"))
    bestHeuristic[start] = 0

    q = [(manhattanD(start, end), 0, *start)] #dist + heur, dist path, r, c

    while len(q):
        m, d, r, c = heappop(q)
        seen.add((r, c))
        if (r, c) == end:
            print(d)
            break

        for dr, dc in DIRECTIONS.values():
            nr, nc = r + dr, c + dc
            if not(0 <= nr <= height and 0 <= nc <= width): continue
            if grid[nr][nc] == "#": continue
            if (nr, nc) in seen: continue

            cost = d + 1
            mand = manhattanD((nr, nc), end)
            heur = cost + mand
            if heur >= bestHeuristic[(nr, nc)]: continue
            heappush(q, (heur, cost, nr, nc))
            bestHeuristic[(nr, nc)] = heur
