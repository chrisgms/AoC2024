from functools import cache

file = "./example1.txt"
file = "./input1.txt"

@cache
def canMakePattern(patterns, design):
    if design == "": return True
    for p in patterns:
        if not(design.startswith(p)): continue
        if canMakePattern(patterns, design[len(p):]): return True
    return False

with open(file) as f:
    patterns, designs = f.read().split("\n\n")
    patterns = patterns.split(", ")
    patterns.sort(key=lambda p: -len(p))
    patterns = tuple(patterns)
    designs = designs.splitlines()

    successes = map(lambda d: canMakePattern(patterns, d), designs)
    print(sum(successes))