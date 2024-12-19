with open('day15\\day15real.txt', 'r') as f:
    raw = f.read()

import numpy as np

raw = raw.replace('#', '##').replace('.', '..').replace('@', '@.').replace('O', '[]')

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

def get_grid_str():
    return '\n'.join([''.join(list(i)) for i in list(grid)])


for direction_char in directions:
    direction = dir_char_to_vec[direction_char]
    stack = []
    queue = [pos.copy()]
    is_blocked = False
    while len(queue) > 0:
        
        current = queue.pop(0) + direction
        current_char = grid[tuple(current)]
        if current_char == '#':
            is_blocked = True
            break
        if current_char == '.':
            continue
        stack.append(current)
        queue.append(current)

        # check for other part of box
        if current_char == '[' and direction_char in ['v', '^']:
            stack.append(current + np.array([0, 1]))
            queue.append(current + np.array([0, 1]))
        elif current_char == ']' and direction_char in ['v', '^']:
            stack.append(current + np.array([0, -1]))
            queue.append(current + np.array([0, -1]))

    if not is_blocked:
        # since not moving on a straight line, easiest is to just make a copy
        new_grid = grid.copy()
        for tile in stack:
            new_grid[tuple(tile)] = '.'
        for tile in stack:
            new_grid[tuple(tile + direction)] = grid[tuple(tile)]
        grid = new_grid
        grid[pos[0], pos[1]] = '.'
        pos = pos + direction
        grid[pos[0], pos[1]] = '@'


result = 0
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == '[':
            result += (100 * i) + j

print(result)