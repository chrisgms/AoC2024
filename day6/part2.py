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

def calculatePath(board, start):
    uniqueVisited = set()
    visited = set()

    currentPos = (*start, "^")

    while currentPos not in visited:
        r, c, dir = currentPos
        board[r][c] = dir
        
        visited.add(currentPos)
        uniqueVisited.add((r, c))
        
        dr, dc = positionDeltas[dir]
        nextr, nextc = r + dr, c + dc

        if not(0 <= nextr < len(board)) or not(0 <= nextc < len(board[0])):
            return False, uniqueVisited
        elif board[nextr][nextc] == "#":
            currentPos = (r, c, rotations[dir])
        else:
            currentPos = (nextr, nextc, dir)
    
    return True, 1
    

# with open("./example1.txt") as f:
with open("./input1.txt") as f:
    board = [list(l) for l in f.read().splitlines()]
    startingPosition = getStartingPosition(board)

    path = calculatePath(board, startingPosition)[1]

    loops = 0
    for pos in path:
        if pos != startingPosition:
            r, c = pos
            board[r][c] = "#"
            if calculatePath(board, startingPosition)[0]:
                loops += 1
            board[r][c] = "."
    
    print(loops)
