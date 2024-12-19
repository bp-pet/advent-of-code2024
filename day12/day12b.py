"""Reworked from part A: added padding so that we can always get all neighbors, and made neighbors be added in a clockwise order."""

with open('day12real.txt', 'r') as f:
    raw = f.read()

import numpy as np

grid = np.array([list(i) for i in raw.split('\n')])

# add padding
grid = np.concatenate([np.full([grid.shape[0], 1], '.'), grid, np.full([grid.shape[0], 1], '.')], axis=1)
grid = np.concatenate([np.full([1, grid.shape[1]], '.'), grid, np.full([1, grid.shape[1]], '.')], axis=0)

def get_neighbors(pos):
    result = []
    if pos[0] != 0:
        result.append((pos[0] - 1, pos[1]))
    if pos[1] != 0:
        result.append((pos[0], pos[1] - 1))
    if pos[0] != grid.shape[0] - 1:
        result.append((pos[0] + 1, pos[1]))
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
    corners = 0
    queue = [start]
    visited = []
    while len(queue) > 0:
        current = queue.pop(0)
        all_neighbors = get_neighbors(current)
        for neighbor in all_neighbors:
            if grid[neighbor] == grid[current]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
        for i in range(4):
            """Basically for each pair of adjacent neighbors, if they are both of a different color, then it's a corner. Also if they are both of the same color, but the diagonal neighbor between them is of the same color, then it's a (concave) corner. Each corner corresponds to exactly 1 side. This can be shown easily on paper."""
            n1 = all_neighbors[i - 1]
            n2 = all_neighbors[i]
            if grid[n1] != grid[current] and grid[n2] != grid[current]:
                corners += 1
                continue
            if grid[n1] == grid[current] and grid[n2] == grid[current] and grid[tuple(np.array(n2) + np.array(n1) - np.array(current))] != grid[current]:
                corners += 1

        area += 1
        visited.append(current)
    for v in visited:
        grid[v] = '.'
    return area * corners


result = 0
while True:
    start = find_unprocessed()
    if start is None:
        break
    result += get_value(start)

print(result)