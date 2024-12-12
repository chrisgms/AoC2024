from collections import deque

file = "./example1.txt"
file = "./input1.txt"

def regionBFS(board, seen, sr, sc):
    area = 0
    perimeter = 0
    q = deque([(sr, sc)])
    while len(q):
        r, c = q.popleft()
        plant = board[r][c]
        area += 1
        perimeter += 4
        

        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not(0 <= nr < len(board) and 0 <= nc < len(board[0])): continue
            p = board[nr][nc]
            if p != plant: continue
            perimeter -= 1
            if (nr, nc) not in seen: 
                seen.add((nr, nc))
                q.append((nr, nc))
    return (area, perimeter)
                

with open(file) as f:
    board = f.read().splitlines()

    cost = 0
    seen = set()

    for r, row in enumerate(board):
        for c, plant in enumerate(row):
            if (r, c) in seen: continue
            seen.add((r, c))
            a, p = regionBFS(board, seen, r, c)
            cost += a * p

    print(cost)
