with open('day04\\day04real.txt') as f:
    raw = f.read()

import numpy as np

data = np.array([list(i) for i in raw.split('\n')])

# add padding
data = np.concatenate([np.array([['.'] * data.shape[1]]), data], axis=0)
data = np.concatenate([np.array([['.']] * data.shape[0]), data], axis=1)

def check_array(a):
    return 1 if ''.join(a) == 'XMAS' else 0
    

result = 0
for i in range(1, data.shape[0]):
    for j in range(1, data.shape[1]):
        result += check_array(data[i,j:j+4])
        result += check_array(data[i:i+4,j])
        result += check_array(data[i,j:j-4:-1])
        result += check_array(data[i:i-4:-1,j])
        result += check_array(data[i:i+4,j:j+4].diagonal())
        result += check_array(data[i:i+4,j:j-4:-1].diagonal())
        result += check_array(data[i:i-4:-1,j:j+4].diagonal())
        result += check_array(data[i:i-4:-1,j:j-4:-1].diagonal())


print(result)