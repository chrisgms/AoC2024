from collections import defaultdict

def checkOrder(precedence, order):
    for i, p1 in enumerate(order):
        for p2 in order[i+1:]:
            if p1 in precedence[p2]:
                return 0
    return int(order[len(order)//2])

# with open("./example1.txt") as f:
with open("./input1.txt") as f:
    rules, updates = [l.splitlines() for l in f.read().split("\n\n")]
    
    precedence = defaultdict(list)

    for p1, p2 in [r.split("|") for r in rules]:
        precedence[p1].append(p2)

    middles = 0

    for u in updates:
        order = u.split(",")
        middles += checkOrder(precedence, order)

    print(middles)