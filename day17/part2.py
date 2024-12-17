file = "./example2.txt"
file = "./input1.txt"

def buildInitialValue(instructions, idx, currValue):
    if idx < 0: return currValue

    currIns = instructions[idx]
    for i in range(8):
        candidate = (currValue << 3) | i
        A = candidate
        B = 0
        C = 0
        B = A % 8
        B = B ^ 3
        C = A >> B
        B = B ^ C
        A = A >> 3
        B = B ^ 5
        B = B % 8
        if B == currIns:
            result = buildInitialValue(instructions, idx - 1, candidate)
            if result: return result

    return None

with open(file) as f:
    _, instructionBlock = f.read().split("\n\n")

    instructions = list(map(int, instructionBlock.split(":")[1].split(",")))
    
    print(buildInitialValue(instructions, len(instructions) - 1, 0))

    
            

