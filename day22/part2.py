from functools import cache
from collections import defaultdict

file = "./example2.txt"
file = "./input1.txt"

modulo = 16777216

@cache
def rotateSecret(secret):
    secret = secret ^ (secret * 64)
    secret %= modulo
    secret = secret ^ (secret // 32)
    secret %= modulo
    secret = secret ^ (secret * 2048)
    secret %= modulo
    return secret

with open(file) as f:
    secrets = [int(l) for l in f.read().splitlines()]
    uniqueSequences = set()
    sequenceResults = defaultdict(dict)
    for secret in secrets:
        origSecret = secret
        diffs = [secret % 10]
        for _ in range(2000):
            secret = rotateSecret(secret)
            diffs.append(secret % 10)
        
        for i in range(0, len(diffs) - 4):
            a, b, c, d, e = diffs[i: i+5]
            sequence = (b - a, c - b, d - c, e - d)
            uniqueSequences.add(sequence)
            if sequence not in sequenceResults[origSecret]:
                sequenceResults[origSecret][sequence] = e

    bestBananas = float("-inf")
    for sequence in uniqueSequences:
        bananas = 0
        for secret in secrets:
            bananas += sequenceResults[secret].get(sequence, 0)
        bestBananas = max(bestBananas, bananas)
    
    print(bestBananas)