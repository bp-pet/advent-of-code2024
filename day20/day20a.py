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

for i in range(maze_num.shape[0]):
    for j in range(maze_num.shape[1]):
        if maze_num[i, j] != -1:
            continue
        current = np.array([i, j])
        neighbors = []
        for offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            try:
                if maze_num[tuple(current + np.array(offset))] != -1:
                    neighbors += [current + np.array(offset)]
            except IndexError:
                continue
        if neighbors == []:
            continue
        min_pos = min(neighbors, key=lambda x: maze_num[tuple(x)])
        max_pos = max(neighbors, key=lambda x: maze_num[tuple(x)])
        if (min_pos == max_pos).all():
            continue
        diff = maze_num[tuple(max_pos)] - maze_num[tuple(min_pos)] - 2
        if diff >= 100:
            result += 1

print(result)