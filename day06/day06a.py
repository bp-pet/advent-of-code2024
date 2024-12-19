with open('day06\\day06real.txt', 'r') as f:
    raw = f.read()

import numpy as np

maze = np.array([list(i) for i in raw.split('\n')])

for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] in ['^', 'v', '<', '>']:
            pos = [i, j]
            if maze[i, j] == '^':
                direc = [-1, 0]
            elif maze[i, j] == 'v':
                direc = [1, 0]
            elif maze[i, j] == '>':
                direc = [0, 1]
            elif maze[i, j] == '<':
                direc = [0, -1]
            break

pos = np.array(pos)
direc = np.array(direc)

while True:
    maze[pos[0], pos[1]] = 'o'
    new_pos = pos + direc
    if new_pos[0] in [-1, maze.shape[0]] or new_pos[1] in [-1, maze.shape[1]]:
        # exit
        break
    elif maze[new_pos[0], new_pos[1]] == '#':
        # turn
        if direc[0] == -1:
            direc = np.array([0, 1])
        elif direc[0] == 1:
            direc = np.array([0, -1])
        elif direc[1] == 1:
            direc = np.array([1, 0])
        elif direc[1] == -1:
            direc = np.array([-1, 0])
        continue
    else:
        # keep going
        pos = new_pos

counter = 0
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] == 'o':
            counter += 1

print(counter)