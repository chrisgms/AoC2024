file = "./example1.txt"
file = "./input1.txt"

DIRECTIONS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

def canMoveVertical(board, r, c, dir):
    loc = board[r][c]
    dr, _ = DIRECTIONS[dir]
    nr = r + dr
    partnerC = c - 1
    if loc == "[":
        partnerC = c + 1

    nextLoc1 = board[nr][c]
    nextLoc2 = board[nr][partnerC]

    if nextLoc1 == "#" or nextLoc2 == "#": return False
    elif nextLoc1 == "." and nextLoc2 == ".": return True
    elif nextLoc1 == loc: return canMoveVertical(board, nr, c, dir)
    elif nextLoc1 == ".": return canMoveVertical(board, nr, partnerC, dir)
    elif nextLoc2 == ".": return canMoveVertical(board, nr, c, dir)
    else: return canMoveVertical(board, nr, partnerC, dir) and canMoveVertical(board, nr, c, dir)

def shiftBoxesVertical(board, r, c, dir):
    loc = board[r][c]
    dr, _ = DIRECTIONS[dir]
    nr = r + dr
    partnerC = c - 1
    if loc == "[":
        partnerC = c + 1

    nextLoc1 = board[nr][c]
    nextLoc2 = board[nr][partnerC]

    if not(nextLoc1 == "." and nextLoc2 == "."):
        if nextLoc1 == loc: shiftBoxesVertical(board, nr, c, dir)
        elif nextLoc1 == ".": shiftBoxesVertical(board, nr, partnerC, dir)
        elif nextLoc2 == ".": shiftBoxesVertical(board, nr, c, dir)
        else: 
            shiftBoxesVertical(board, nr, partnerC, dir)
            shiftBoxesVertical(board, nr, c, dir)
    
    board[r][c], board[nr][c] = board[nr][c], board[r][c]
    board[r][partnerC], board[nr][partnerC] = board[nr][partnerC], board[r][partnerC]

def shiftBoxes(board, r, c, dir):
    if dir in ["^", "v"]: 
        dr, _ = DIRECTIONS[dir]
        if canMoveVertical(board, r + dr, c, dir): 
            shiftBoxesVertical(board, r + dr, c, dir)
            return (r + dr, c)
        return (r, c)
    steps = 0
    dr, dc = DIRECTIONS[dir]
    endR, endC = r + dr, c + dc
    while 0 <= endR < len(board) and 0 <= endC < len(board[0]):
        steps += 1
        if board[endR][endC] == "#": break
        if board[endR][endC] == ".": 
            for _ in range(steps):
                prevR, prevC = endR - dr, endC - dc
                board[endR][endC], board[prevR][prevC] = board[prevR][prevC], board[endR][endC]
                endR, endC = prevR, prevC
            r, c = r + dr, c + dc
            break
        endR, endC = endR + dr, endC + dc
    return (r, c)

with open(file) as f:
    board, instructions = f.read().split("\n\n")
    board = [list("".join([{"#": "##", "O": "[]", ".": "..", "@": "@."}[ch] for ch in l])) for l in board.splitlines()]
    instructions = instructions.replace("\n", "")

    position = (0, 0)
    for r, row in enumerate(board):
        for c, loc in enumerate(row):
            if loc == "@": 
                position = (r, c)
                break

    for instruction in instructions:
        dr, dc = DIRECTIONS[instruction]
        r, c = position
        lr, lc = r + dr, c + dc
        loc = board[lr][lc]
        if loc == "#": continue
        elif loc in ["[", "]"]:
            nextPos = shiftBoxes(board, r, c, instruction)
            if instruction in ["^", "v"] and nextPos != position:
                board[lr][lc], board[r][c] = board[r][c], board[lr][lc]
            position = nextPos
        else:
            board[lr][lc], board[r][c] = board[r][c], board[lr][lc]
            position = (lr, lc)

    gps = 0
    for r, row in enumerate(board):
        for c, loc in enumerate(row):
            if loc == "[":
                gps += r * 100 + c
    print(gps)
    
    