from functools import cache

file = "./example1.txt"
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
    res = 0
    for secret in secrets:
        for _ in range(2000):
            secret = rotateSecret(secret)
        res += secret

    print(res)