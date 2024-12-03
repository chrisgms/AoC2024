def reportIsSafe(report):
    diffs = [y - x for x, y in zip(report, report[1:])]
    return all(1 <= abs(x) <= 3 for x in diffs) and all(x*y > 0 for x,y in zip(diffs, diffs[1:]))

with open("./input1.txt") as f:
    reports = [list(map(int, l.split())) for l in  f.readlines()]

    safe = 0
    for r in reports:
        if reportIsSafe(r):
            safe += 1
    print(safe)