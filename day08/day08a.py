with open('day08\\day08real.txt', 'r') as f:
    raw = f.read()

import numpy as np

field = np.array([list(i) for i in raw.split('\n')])

antenna_locations = {}
for i in range(field.shape[0]):
    for j in range(field.shape[1]):
        content = field[i, j]
        if content == '.':
            continue
        if content not in antenna_locations:
            antenna_locations[content] = [np.array([[i, j]])]
        else:
            antenna_locations[content].append(np.array([[i, j]]))

def check_loc_in_bounds(loc):
    return loc[0][0] >= 0 and loc[0][0] < field.shape[0] and loc[0][1] >= 0 and loc[0][1] < field.shape[1]

antinodes = np.array([[0, 0]])
for antenna in antenna_locations:
    locations = antenna_locations[antenna]
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            loc1, loc2 = locations[i], locations[j]
            new_loc1 = loc1 - (loc2 - loc1)
            new_loc2 = loc2 - (loc1 - loc2)
            if check_loc_in_bounds(new_loc1):
                antinodes = np.concatenate([antinodes, new_loc1], axis=0)
            if check_loc_in_bounds(new_loc2):
                antinodes = np.concatenate([antinodes, new_loc2], axis=0)

result = np.unique(antinodes[1:,:], axis=0)

print(result.shape[0])