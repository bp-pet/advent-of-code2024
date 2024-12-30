"""
Thought the question said that one couldn't exit and re-enter a wall during a cheat.
"""
import numpy as np

with open('day20\\day20real.txt', 'r') as f:
    raw = f.read()

maze = np.array([list(i) for i in raw.split('\n')])

current, end = None, None
maze_num = np.full(maze.shape, -1)

for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] == 'S':
            current = np.array((i, j))
        if maze[i, j] == 'E':
            end = np.array((i, j))
        if maze[i, j] in ['.', 'S', 'E']:
            maze_num[i, j] = -2

counter = 0
while True:
    maze_num[tuple(current)] = counter
    neighbor = None
    for offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if maze_num[tuple(current + np.array(offset))] == -2:
            neighbor = current + np.array(offset)
            break
    if neighbor is None:
        break
    current = neighbor
    counter += 1

result = 0
for start_pos in np.ndindex(maze.shape):
    if maze_num[start_pos] == -1:
        # not a tile
        continue
    for i in range(-20, 21):
        for j in range(-20, 21):
            if abs(i) + abs(j) > 20:
                # too far away
                continue
            end_pos = (start_pos[0] + i, start_pos[1] + j)
            if end_pos[0] < 0 or end_pos[0] >= maze.shape[0] or end_pos[1] < 0 or end_pos[1] >= maze.shape[1]:
                # out of bounds
                continue
            start_val = maze_num[start_pos]
            end_val = maze_num[end_pos]
            saved_amt = end_val - start_val - abs(i) - abs(j)
            if saved_amt >= 100:
                result += 1
print(result)