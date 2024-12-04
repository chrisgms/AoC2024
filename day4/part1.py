neighbors = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1,1],
    [1, 0],
    [1, -1],
    [0, -1]
]

patternMatch = {
    1: "M",
    2: "A",
    3: "S"
}

def xmasDFS(board, r, c, matchedSoFar, dirr=0, dirc=0):
    if (matchedSoFar == 4): 
        return 1

    matches = 0
    for dr, dc in neighbors:
        cr = r + dr
        cc = c + dc
        if 0 <= cr < len(board) and 0 <= cc < len(board[0]) and (matchedSoFar == 1 or dr == dirr and dc == dirc):
            val = board[cr][cc]
            if (val == patternMatch[matchedSoFar]):
                matches += xmasDFS(board, cr, cc, matchedSoFar + 1, dr, dc)
    return matches

# with open("./example1.txt") as f:
with open("./input1.txt") as f:
    board  = [l.strip() for l in f.readlines()]

    total = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if (board[r][c] == "X"):
                total += xmasDFS(board, r, c, 1)
    print(total)