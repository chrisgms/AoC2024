import sys
sys.path.insert(0, '..')

from utils import DIRECTIONS, inBounds
from collections import defaultdict
from heapq import heappop, heappush

file = "./example1.txt"
file = "./input1.txt"

def dijkstraWithDistances(grid, start, end):
    seen = set([start])
    q = [(0, start)]
    distances = defaultdict(int)
    distances[start] = 0

    while len(q):
        d, (r, c) = heappop(q)

        if (r, c) == end:
            break

        seen.add((r,c ))
        
        for dr, dc in DIRECTIONS.values():
            nr, nc = r + dr, c + dc
            if not inBounds(grid, nr, nc): continue
            if (nr, nc) in seen: continue
            if grid[nr][nc] == "#": continue
            heappush(q, (d + 1, (nr, nc)))
            distances[(nr, nc)] = d + 1
    
    return distances


with open(file) as f:
    grid = [list(l) for l in f.read().splitlines()]

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S": start = (r, c)
            if col == "E": end = (r, c)
    

    bestDistances = dijkstraWithDistances(grid, start, end)
    
    count = 0
    for (r, c), d in bestDistances.items():
        for dr, dc in [(-2,0), (-1, 1), (0, 2), (1, 1), (2, 0), (1, -1), (0, -2), (-1, -1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in bestDistances: continue

            newDist = d + 2
            if bestDistances[(nr, nc)] - newDist >= 100: count += 1
    
    print(count)


    
   