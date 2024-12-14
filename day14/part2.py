file = "./example1.txt"
file = "./input1.txt"

def pairWiseDiff(positions):
    diffX = 0
    diffY = 0
    for i in range(len(positions)):
        for j in range(i, len(positions)):
            diffX += abs(positions[i][0] - positions[j][0])
            diffY += abs(positions[i][1] - positions[j][1])
    return diffX, diffY

with open(file) as f:
    robots = []
    for l in f.read().splitlines():
        pos, vel = l.split(" ")
        x, y = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append([x, y, vx, vy])

    width = 101
    height = 103
    seconds = 0
    # while True:
    #     if seconds % 1000 == 0: print(seconds)
    #     if seconds > 10_000: break
    #     seconds += 1
    #     for i, (x, y, vx, vy) in enumerate(robots):
    #         robots[i][0] = (x + vx) % width
    #         robots[i][1] = (y + vy) % height


    #     dx, dy = pairWiseDiff(robots)
    #     if dy < 3_000_000 and dx < 3_000_000:
    #         print(seconds)

    # 6668 had minimal residuals in both dirs
    seconds = 6668
    for i, (x, y, vx, vy) in enumerate(robots):
            robots[i][0] = (x + seconds * vx) % width
            robots[i][1] = (y + seconds * vy) % height
    
    board = [["."] * width for _ in range(height)] 
    for (x, y, _, _) in robots:
        board[y][x] = "#"
    for r in board:
        print("".join(r))


