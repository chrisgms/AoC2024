import math

file = "./example1.txt"
file = "./input1.txt"

def splitStone(stone, depth = 0):
    if depth == 25:
        return 1

    if stone == 0:
        return splitStone(stone + 1, depth + 1)
    
    digits = math.floor(math.log(stone, 10)) + 1
    if digits % 2 == 0:
        left = stone // 10 ** (digits // 2)
        right = stone % 10 ** (digits // 2)
        return splitStone(left, depth+1) + splitStone(right, depth+1)
    
    return splitStone(stone * 2024, depth + 1)

    

with open(file) as f:
    stones = [int(n) for n in f.read().split()]
    score = 0
    for stone in stones:
        score += splitStone(stone)
    print(score)
