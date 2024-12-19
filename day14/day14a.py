from typing import List
import numpy as np

with open('day14\\day14real.txt', 'r') as f:
    raw = f.read()

space_size = np.array([103, 101])

def process_robot_raw(s):
    a = s.split('=')[1].split(',')[0]
    b = s.split(',')[1].split(' ')[0]
    c = s.split('=')[2].split(',')[0]
    d = s.split(',')[2]
    return np.array([int(b), int(a)]), np.array([int(d), int(c)])


class Robot:
    def __init__(self, loc, vel):
        self.loc, self.vel = loc, vel
    
    def move(self, space_size):
        self.loc = (self.loc + self.vel) % space_size
    
    def __str__(self):
        return f'Robot at {self.loc} with velocity {self.vel}'

class Space:
    def __init__(self, size, robots: List[Robot]):
        self.size = size
        self.robots = robots
    
    def move_all(self):
        [robot.move(self.size) for robot in self.robots]

    def move_all_n_times(self, n: int):
        [self.move_all() for _ in range(n)]
    
    def get_grid(self):
        grid = np.zeros(self.size)
        for robot in self.robots:
            grid[robot.loc[0], robot.loc[1]] += 1
        return grid
    
    def get_coefficient(self):
        grid = self.get_grid()
        a = grid[:self.size[0] // 2, :self.size[1] // 2].sum()
        b = grid[:self.size[0] // 2, self.size[1] // 2 + 1:].sum()
        c = grid[self.size[0] // 2 + 1:, :self.size[1] // 2].sum()
        d = grid[self.size[0] // 2 + 1:, self.size[1] // 2 + 1:].sum()
        return int(a * b * c * d)
    
    def __str__(self):
        return f'Space with size {self.size}; robots:\n' + ''.join([str(robot) + '\n' for robot in self.robots])


robots = []
for line in raw.split('\n'):
    loc, vel = process_robot_raw(line)
    robots.append(Robot(loc, vel))

space = Space(space_size, robots)
space.move_all_n_times(100)
print(space.get_coefficient())