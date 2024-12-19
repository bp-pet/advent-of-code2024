with open('day15\\day15real.txt', 'r') as f:
    raw = f.read()

import numpy as np

grid_raw = raw.split('\n\n')[0]
grid = np.array([list(i) for i in grid_raw.split('\n')])

directions_raw = raw.split('\n\n')[1]
directions = ''.join(directions_raw.split('\n'))

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == '@':
            pos = np.array([i, j])
            break

dir_char_to_vec = {'>': np.array([0, 1]), '<': np.array([0, -1]), 'v': np.array([1, 0]), '^': np.array([-1, 0])}

for direction_char in directions:
    direction = dir_char_to_vec[direction_char]
    stack = []
    current = pos.copy()
    is_blocked = False
    while True:
        current = current + direction
        if grid[current[0], current[1]] == '#':
            is_blocked = True
            break
        stack.append(current)
        if grid[current[0], current[1]] == '.':
            break
    if not is_blocked:
        for tile in stack:
            grid[tile[0], tile[1]] = 'O'
        grid[pos[0], pos[1]] = '.'
        pos = pos + direction
        grid[pos[0], pos[1]] = '@'


result = 0
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == 'O':
            result += (100 * i) + j

print(result)