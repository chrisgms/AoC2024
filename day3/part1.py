import re

regex = r"mul\((\d{1,3},\d{1,3})\)"

# with open("./example1.txt") as f:
with open("./input1.txt") as f:
    sum = 0
    for match in re.findall(regex, f.read()):
        op1, op2 = map(int, match.split(","))
        sum += op1 * op2
    print(sum)