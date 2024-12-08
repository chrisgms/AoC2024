from collections import defaultdict

# file = "./example1.txt"
file = "./input1.txt"

with open(file) as f:
    board = [list(l) for l in f.read().splitlines()]

    antennas = defaultdict(list)

    for r, row in enumerate(board):
        for c, ant in enumerate(row):
            if ant != ".":
                antennas[ant].append((r, c))


    nodes = set()
    for v in antennas.values():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                r1, c1 = v[i]
                r2, c2 = v[j]
                
                dr = r2 - r1
                dc = c2 - c1

                n1r, n1c = r1 - dr, c1 - dc
                n2r, n2c = r2 + dr, c2 + dc
                nodes.add((r1, c1))
                nodes.add((r2, c2))
                while 0 <= n1r < len(board) and 0 <= n1c < len(board[0]):
                    nodes.add((n1r, n1c))
                    n1r, n1c = n1r - dr, n1c - dc
                while 0 <= n2r < len(board) and 0 <= n2c < len(board[0]):
                    nodes.add((n2r, n2c))
                    n2r, n2c = n2r + dr, n2c + dc


    print(len(nodes))
    
