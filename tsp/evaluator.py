import re
from pathlib import Path
from django.conf import settings

path = Path(settings.BASE_DIR) / 'tsp' / 'static' / 'input.txt'
with open(path, 'r') as f:
    lines = f.readlines()

n = int(lines[0].strip())
points = [(x, y) for x, y in (map(int, line.strip().split()) for line in lines[1:n+1])]

def evaluate(tour):
    result = 0
    for a, b in zip(tour, tour[1:] + [tour[0]]):
        xa, ya = points[a]
        xb, yb = points[b]
        result += ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    return result
    
def evaluate_text(input):
    match = re.match(r'\d+( \d+)+', input.strip())
    if not match: raise ValueError('Invalid input format')
    
    tour = list(map(int, input.strip().split()))
    if len(tour) != n: raise ValueError('Tour length does not match number of points')
    if set(tour) != set(range(n)): raise ValueError('Tour must include all points exactly once')

    return evaluate(tour)
