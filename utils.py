DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

def inBounds(matrix, r, c):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])