import sys
sys.path.insert(0, '..')

from utils import DIRECTIONS, inBounds
from collections import defaultdict, deque
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

def reachablePathNodes(grid, start):
    seen = set([start])
    q = deque([(start, 0)])

    while len(q):
        (r, c), d = q.popleft()
        if d > 19: break
        for dr, dc in DIRECTIONS.values():
            nr, nc = r + dr, c + dc
            if not inBounds(grid, nr, nc): continue
            if (nr, nc) in seen: continue
            q.append(((nr, nc), d + 1))
            seen.add((nr, nc))

    return seen

def manhattanD(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return abs(r2 - r1) + abs(c2 - c1)


with open(file) as f:
    grid = [list(l) for l in f.read().splitlines()]

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S": start = (r, c)
            if col == "E": end = (r, c)
    

    bestDistances = dijkstraWithDistances(grid, start, end)
    
    count = 0
    for start, d in bestDistances.items():
        for end in reachablePathNodes(grid, start):
            if end not in bestDistances: continue

            newDist = d + manhattanD(start, end)
            if bestDistances[end] - newDist >= 100: count += 1
    
    print(count)


    
   