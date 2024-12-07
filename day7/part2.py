import itertools

def multiply(a, b):
   return a * b

def add(a, b):
   return a + b

def concat(a, b):
    return int(str(a) + str(b))


file = "./example1.txt"
file = "./input1.txt"

with open(file) as f:
    equations = f.read().splitlines()

    operators = [multiply, add, concat]

    total = 0
    for eq in equations:
        result, operands = eq.split(":")
        result = int(result)
        operands = list(map(int, operands.strip().split()))[::-1]
      
        operatorCombos = map(list, itertools.product(operators, repeat=len(operands) - 1))

        for combo in operatorCombos:
            nums = operands.copy()
            while len(nums) > 1:
                a = nums.pop()
                b = nums.pop()
                op = combo.pop()
                nums.append(op(a,b))
            if nums[0] == result:
                total += result
                break

    print(total)