import re

regex = r"don't\(\)|do\(\)|mul\((\d{1,3},\d{1,3})\)"

# with open("./example2.txt") as f:
with open("./input1.txt") as f:
    sum = 0
    enabled = 1
    for match in re.finditer(regex, f.read()):
        group = match.group()
        if group.startswith("don't"):
            enabled = 0
        elif group.startswith("do"):
            enabled = 1
        else:
            op1, op2 = map(int, match.groups()[0].split(","))
            sum += op1 * op2 * enabled
    print(sum)