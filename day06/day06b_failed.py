"""First thought about at each step sending a ray to the left, which if later stepped on (in the same direction) would mean there is a possible loop there. This would be a very optimal solutions but too many edge cases to consider so maybe not possible.

Then tried at each step to simulate a right turn and check if that causes a loop. I don't remember why it didn't work but either way it wouldn't be considerably faster than the brute-force method. Actually I remember why. Simulating a right turn by itself is not enough, one would have to also place a temporary wall where the turn is, as the alternative (newly created) route might interact with that tile. Again, this basically makes it the same solution as the brute force (slightly faster but still)."""

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
            pos = (i, j)
            start_pos = (i, j) # cannot put blocks on it so has to be saved separately
            direc_vec = sym_to_vec[maze[i, j]]
            break

def check_pos_in_bounds(pos):
    return pos[0] >= 0 and pos[0] < maze.shape[0] and pos[1] >= 0 and pos[1] < maze.shape[1]

def add_vec_to_pos(pos, vec):
    return (pos[0] + vec[0], pos[1] + vec[1])

options = []

# saving multiple directions for each tile in case of u-turns
footsteps = {}

counter = 0

while True:

    # update footsteps
    if pos not in footsteps:
        footsteps[pos] = [vec_to_sym[direc_vec]]
    else:
        footsteps[pos].append(vec_to_sym[direc_vec])
    
    # calculate next tile
    new_pos = add_vec_to_pos(pos, direc_vec)

    # check for exit
    if not check_pos_in_bounds(new_pos):
        break

    # check for turn
    elif maze[new_pos] == '#':
        direc_vec = turn_right_direc_vec(direc_vec)
        continue

    # otherwise continue forward
    else:

        # send temp ray to the right (same procedure but with temporary data storage)
        temp_direc_vec = turn_right_direc_vec(direc_vec)
        temp_pos = pos
        temp_footsteps = {}
        while True:
            if temp_pos not in temp_footsteps:
                temp_footsteps[temp_pos] = [vec_to_sym[temp_direc_vec]]
            else:
                temp_footsteps[temp_pos].append(vec_to_sym[temp_direc_vec])
            
            temp_new_pos = add_vec_to_pos(temp_pos, temp_direc_vec)
            if not check_pos_in_bounds(temp_new_pos):
                break
            elif maze[temp_new_pos] == '#':
                temp_direc_vec = turn_right_direc_vec(temp_direc_vec)
                continue
            elif (temp_pos in footsteps and vec_to_sym[temp_direc_vec] in footsteps[temp_pos]) or (temp_pos in temp_footsteps and vec_to_sym[temp_direc_vec] in temp_footsteps[temp_pos]):
                # loop found
                if new_pos != start_pos and new_pos not in footsteps: # cannot put block on start pos or footsteps
                    options.append(new_pos)
                break
            else:
                temp_pos = temp_new_pos
                continue

        # keep going
        pos = new_pos

# might be duplicates so take set
print(len(set(options)))