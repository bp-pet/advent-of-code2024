with open('day04\\day04real.txt') as f:
    raw = f.read()

import numpy as np

data = np.array([list(i) for i in raw.split('\n')])

# add padding
data = np.concatenate([np.array([['.'] * data.shape[1]]), data, np.array([['.'] * data.shape[1]])], axis=0)
data = np.concatenate([np.array([['.']] * data.shape[0]), data, np.array([['.']] * data.shape[0])], axis=1)

def check_array(a):
    return 1 if ''.join(a) in ['MAS', 'SAM'] else 0

result = 0
for i in range(1, data.shape[0] - 1):
    for j in range(1, data.shape[1] - 1):
        result += ((
            check_array(data[i-1:i+2,j-1:j+2].diagonal())
            + check_array(data[i-1:i+2,j+1:j-2:-1].diagonal())
        ) > 1)


print(result)