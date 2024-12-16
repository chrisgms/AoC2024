from heapq import heappush, heappop

file = "./example1.txt"
file = "./example2.txt"
file = "./input1.txt"

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

ROTATIONS = ["^", ">", "v", "<"]


def getRotationCost(dir1, dir2):
    steps = abs(ROTATIONS.index(dir1) - ROTATIONS.index(dir2))
    if steps == 0: return 0
    if steps == 1 or steps == 3: return 1000
    return 2000

def rotatingDijkstra(board, start, end, direction):
    q = [(0, *start, direction, set())]
    seen = set()

    minEnd = float("inf")
    endPaths = set()
    while len(q):
        d, r, c, dir, path = heappop(q)
        path.add((r, c))
        seen.add((r, c, dir))

        if (r, c) == end:
            if d > minEnd: return minEnd, len(endPaths)
            minEnd = d
            endPaths |= path
        
        if (r, c) != end and len(endPaths) > 0: return minEnd, len(endPaths)
        
        for ndir, (dr, dc) in DIRECTIONS.items():
            nr, nc = r + dr, c + dc
            if not(0 <= nr < len(board) and 0 <= nc < len(board[0])): continue
            if (nr, nc, ndir) in seen: continue
            if board[nr][nc] == "#": continue
            cost = d + 1 + getRotationCost(dir, ndir)
            heappush(q, (cost, nr, nc, ndir, path.copy()))

with open(file) as f:
    board = f.read().splitlines()

    dir = ">"
    start = (-1, -1)
    end = (-1, -1)
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == "S": start = (r, c)
            if col == "E": end = (r, c)

    print(rotatingDijkstra(board, start, end, dir))