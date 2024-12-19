"""Just using brute-force: finding path separately for each possible location of extra wall. Tried some alternatives to solve it in a smarter way but doesn't seem feasible."""

with open('day06\\day06real.txt', 'r') as f:
    raw = f.read()

import numpy as np

maze = np.array([list(i) for i in raw.split('\n')])

sym_to_vec = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
vec_to_sym = {sym_to_vec[i]: i for i in sym_to_vec}
turn_right_sym = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def turn_right_direc_vec(vec):
    return sym_to_vec[turn_right_sym[vec_to_sym[vec]]]

for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] in ['^', 'v', '<', '>']:
            start_pos = (i, j)
            start_direc = maze[i, j]
            break

def check_pos_in_bounds(pos):
    return pos[0] >= 0 and pos[0] < maze.shape[0] and pos[1] >= 0 and pos[1] < maze.shape[1]

def add_vec_to_pos(pos, vec):
    return (pos[0] + vec[0], pos[1] + vec[1])

def has_loop():
    footsteps = np.zeros([maze.shape[0], maze.shape[1]])
    pos = start_pos
    direc_vec = sym_to_vec[start_direc]
    while True:
        
        # calculate next tile
        new_pos = add_vec_to_pos(pos, direc_vec)

        # check for exit
        if not check_pos_in_bounds(new_pos):
            footsteps[pos] += 1
            return footsteps

        # check for turn
        elif maze[new_pos] in ['#', 'o']:
            direc_vec = turn_right_direc_vec(direc_vec)
            continue

        # check for loop
        elif footsteps[pos] >= 4:
            return None

        # otherwise continue forward
        else:
            # keep going
            footsteps[pos] += 1
            pos = new_pos

options = np.argwhere(has_loop() > 0)

result = 0
for i in range(options.shape[0]):
    option = tuple(options[i, :])
    if option != start_pos:
        maze[option] = 'o'
        path = has_loop()
        if path is None:
            result += 1
        maze[option] = '.'

print(result)