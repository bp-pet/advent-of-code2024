with open('day12\\day12real.txt', 'r') as f:
    raw = f.read()

import numpy as np

grid = np.array([list(i) for i in raw.split('\n')])

def get_neighbors(pos):
    result = []
    if pos[0] != 0:
        result.append((pos[0] - 1, pos[1]))
    if pos[0] != grid.shape[0] - 1:
        result.append((pos[0] + 1, pos[1]))
    if pos[1] != 0:
        result.append((pos[0], pos[1] - 1))
    if pos[1] != grid.shape[1] - 1:
        result.append((pos[0], pos[1] + 1))
    return result

def find_unprocessed():
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != '.':
                return (i, j)
    return None

def get_value(start):
    area = 0
    perimeter = 0
    queue = [start]
    visited = []
    while len(queue) > 0:
        current = queue.pop(0)
        all_neighbors = get_neighbors(current)
        for neighbor in all_neighbors:
            if grid[neighbor] == grid[current]:
                perimeter -= 1
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
        perimeter += 4
        area += 1
        visited.append(current)
    for v in visited:
        grid[v] = '.'
    return area * perimeter


result = 0
while True:
    start = find_unprocessed()
    if start is None:
        break
    result += get_value(start)

print(result)