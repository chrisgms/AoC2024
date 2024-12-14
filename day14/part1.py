file = "./example1.txt"
file = "./input1.txt"

with open(file) as f:
    robots = []
    for l in f.read().splitlines():
        pos, vel = l.split(" ")
        x, y = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append([x, y, vx, vy])

    width = 101
    height = 103

    for i, (x, y, vx, vy) in enumerate(robots):
        robots[i][0] = (x + 100 * vx) % width
        robots[i][1] = (y + 100 * vy) % height

    quadrants = [0] * 4
    for (x, y, _, _) in robots:
        if x < width // 2 and y < height // 2:
            quadrants[0] += 1
        elif x < width // 2 and y > height // 2:
            quadrants[1] += 1
        elif x > width // 2 and y < height // 2:
            quadrants[2] += 1
        elif x > width // 2 and y > height // 2:
            quadrants[3] += 1
    
    factor = 1
    for q in quadrants:
        factor *= q
    print(factor)