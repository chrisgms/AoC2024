def getStartingPosition(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "^":
                return (r, c)

positionDeltas = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1],
}

rotations = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}

# with open("./example1.txt") as f:
with open("./input1.txt") as f:
    board = [list(l) for l in f.read().splitlines()]
    startingPosition = getStartingPosition(board)

    uniqueVisited = set()
    visited = set()

    currentPos = (*startingPosition, "^")

    while currentPos not in visited:
        r, c, dir = currentPos
        board[r][c] = dir
        
        visited.add(currentPos)
        uniqueVisited.add((r, c))
        
        dr, dc = positionDeltas[dir]
        nextr, nextc = r + dr, c + dc

        if not(0 <= nextr < len(board)) or not(0 <= nextc < len(board[0])):
            break
        elif board[nextr][nextc] == "#":
            currentPos = (r, c, rotations[dir])
        else:
            currentPos = (nextr, nextc, dir)
    
    print(len(uniqueVisited))
