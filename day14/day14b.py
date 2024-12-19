"""Got stuck on this so checked reddit. Accidentally saw image of result and also found a few solution ideas that I didn't like, so mine is different. Also saw a hint for the period being 101*103, since I had made a mistake and thought it was in the billions, which is what got me stuck in the first place."""

import numpy as np
import matplotlib.pyplot as plt

with open('day14real.txt', 'r') as f:
    raw = f.read()

space_size = np.array([103, 101])


class Space:
    def __init__(self, size: np.array, locs: np.array, vels: np.array) -> None:
        self.size = size
        self.locs = locs
        self.vels = vels
        self.num_robots = locs.shape[0]
    
    def move_all(self) -> None:
        self.locs = (self.locs + self.vels) % self.size

    def move_all_n_times(self, n: int) -> None:
        [self.move_all() for _ in range(n)]

    def get_coefficient(self) -> int:
        """ Count the number of robots that have at least 2 adjacent robots."""
        coefficient = 0
        for r1 in range(self.num_robots):
            found = False
            for r2 in range(r1 + 1, self.num_robots):
                if abs(self.locs[r1, 0] - self.locs[r2, 0]) <= 1 and abs(self.locs[r1, 1] - self.locs[r2, 1]) <= 1:
                    found = True
                    break
            coefficient += 1 if found else 0
        return coefficient
 
    def __str__(self):
        return f'Space with size {self.size}; robots:\n' + ''.join([str(robot) + '\n' for robot in self.robots])


def process_robot_raw(s: str) -> np.array:
    a = s.split('=')[1].split(',')[0]
    b = s.split(',')[1].split(' ')[0]
    c = s.split('=')[2].split(',')[0]
    d = s.split(',')[2]
    return np.array([int(b), int(a)]), np.array([int(d), int(c)])

locs, vels = [], []
for line in raw.split('\n'):
    loc, vel = process_robot_raw(line)
    locs.append(loc)
    vels.append(vel)

space = Space(space_size, np.array(locs), np.array(vels))

max_steps = 101 * 103
vals = []
for i in range(max_steps):
    if i % 100 == 0 and i > 0:
        print(f'Progress: {i} of {max_steps}')
    vals.append(space.get_coefficient())
    space.move_all()

solution = np.argmax(np.array(vals))

print(solution)

space.move_all_n_times(solution)
[plt.scatter(space.locs[r, 0], space.locs[r, 1], s=1, c='r') for r in range(space.locs.shape[0])]
plt.show()