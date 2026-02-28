import random

N = 1000
SEED = 42
AMPLITUDE = 1000

random.seed(SEED)
points = [((random.random() * 2 - 1) * AMPLITUDE, (random.random() * 2 - 1) * AMPLITUDE) for _ in range(N)]

print(N)
for x, y in points:
    print(x, y)
