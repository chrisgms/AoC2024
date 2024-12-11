file = "./example1.txt"
file = "./input1.txt"

def trailBFS(board, sr, sc):
    trailends = 0
    path = [(sr, sc, 0)]
    while len(path):
        r, c, h = path.pop()

        if h == 9:
            trailends += 1
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nextr = r + dr
            nextc = c + dc
            if not(0 <= nextr < len(board) and 0 <= nextc < len(board[0])): continue

            nexth = board[nextr][nextc]

            if nexth == h + 1:
                path.append((nextr, nextc, nexth))
    return trailends


with open(file) as f:
    board = [list(map(int, list(l))) for l in f.read().splitlines()]
    score = 0
    for r, row in enumerate(board):
        for c, height in enumerate(row):
            if height == 0:
                score += trailBFS(board, r, c)
    
    print(score)