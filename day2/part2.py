def reportIsSafe(report):
    diffs = [y - x for x, y in zip(report, report[1:])]
    return all(1 <= abs(x) <= 3 for x in diffs) and all(x*y > 0 for x,y in zip(diffs, diffs[1:]))

with open("./example1.txt") as f:
    reports = [list(map(int, l.split())) for l in  f.readlines()]

    safe = 0
    for r in reports:
        for candidate in [r[:i] + r[i+1:] for i in range(len(r))]:
            if reportIsSafe(candidate):
                safe += 1
                break
    print(safe)