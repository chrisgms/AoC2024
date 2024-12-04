def xmasCheck(board, r, c):
    diag1 = board[r-1][c-1] + board[r+1][c+1]
    diag2 = board[r-1][c+1] + board[r+1][c-1]
    return (diag1 == "MS" or diag1 == "SM") and (diag2 == "MS" or diag2 == "SM")

# with open("./example1.txt") as f:
with open("./input1.txt") as f:
    board  = [l.strip() for l in f.readlines()]

    total = 0
    for r in range(1, len(board) - 1):
        for c in range(1, len(board[0]) - 1):
            if (board[r][c] == "A"):
                if xmasCheck(board, r, c):
                    total += 1
    print(total)