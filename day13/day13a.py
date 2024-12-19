with open('day13\\day13real.txt', 'r') as f:
    raw = f.read()

import re
import numpy as np

result = 0

def get_closest_int(x):
    return int(round(x, 0))

for module_raw in raw.split('\n\n'):
    buttonA_raw = module_raw.split('\n')[0]
    buttonB_raw = module_raw.split('\n')[1]
    prize_raw = module_raw.split('\n')[2]

    elementsA = [int(i[1:]) for i in re.findall(r'\+\d+', buttonA_raw)]
    elementsB = [int(i[1:]) for i in re.findall(r'\+\d+', buttonB_raw)]
    prize = [int(i[1:]) for i in re.findall(r'=\d+', prize_raw)]

    A = np.array([elementsA, elementsB]).transpose()
    b = np.array([prize]).transpose()

    assert np.linalg.matrix_rank(A) == 2

    sol = np.linalg.solve(A, b)

    pressesA, pressesB = get_closest_int(sol[0, 0]), get_closest_int(sol[1, 0])

    if pressesA < 0 or pressesB < 0 or pressesA > 100 or pressesB > 100 or (np.dot(A, np.array([[pressesA], [pressesB]])) != b).any(): # if solution is noninteger, after rounding and doing the dot product, the answer will be different
        continue


    result += 3 * pressesA + pressesB

print(result)