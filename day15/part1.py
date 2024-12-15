file = "./example1.txt"
file = "./input1.txt"

DIRECTIONS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

def shiftBoxes(board, r, c, dir):
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
    board = [list(l) for l in board.splitlines()]
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
        elif loc == "O": position = shiftBoxes(board, r, c, instruction)
        else:
            board[lr][lc], board[r][c] = board[r][c], board[lr][lc]
            position = (lr, lc)

    gps = 0
    for r, row in enumerate(board):
        for c, loc in enumerate(row):
            if loc == "O":
                gps += r * 100 + c
    print(gps)
    
    