file = "./example1.txt"
file = "./input1.txt"

def getComboOperand(registers, operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers[0]
        case 5:
            return registers[1]
        case 6:
            return registers[2]
        case 7:
            raise Exception("unexpected")

with open(file) as f:
    registerBlock, instructionBlock = f.read().split("\n\n")

    registers = registerBlock.splitlines()
    for i, reg in enumerate(registers):
        registers[i] = int(reg.split(":")[1])

    instructions = list(map(int, instructionBlock.split(":")[1].split(",")))

    instructionIdx = 0
    output = []
    while instructionIdx < len(instructions):
        opcode = instructions[instructionIdx]
        operand = instructions[instructionIdx + 1]
        match opcode:
            case 0:
                registers[0] = registers[0] >> getComboOperand(registers, operand)
            case 1:
                registers[1] = registers[1] ^ operand
            case 2:
                registers[1] = getComboOperand(registers, operand) % 8
            case 3:
                if registers[0]:
                    instructionIdx = operand
                    continue
            case 4:
                registers[1] = registers[1] ^ registers[2]
            case 5:
                output.append(getComboOperand(registers, operand) % 8)
            case 6:
                registers[1] = registers[0] >> getComboOperand(registers, operand)
            case 7:
                registers[2] = registers[0] >> getComboOperand(registers, operand)
        
        instructionIdx += 2
    
    print(",".join(map(str, output)))