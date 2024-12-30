import numpy as np

with open('day25\\day25real.txt', 'r') as f:
    raw = f.read()

entities_arrays = np.array([[list(row) for row in entity_raw.split('\n')] for entity_raw in raw.split('\n\n')])


keys = []
locks = []

for entity in entities_arrays:
    counts = []
    for col in range(5):
        count = 0
        for row in range(7):
            if entity[row, col] == '#':
                count += 1
        counts += [count - 1]
    if entity[0, 0] == '#':
        keys.append(counts)
    else:
        locks.append(counts)

result = 0
for lock in locks:
    for key in keys:
        is_match = True
        for col in range(5):
            if lock[col] + key[col] > 5:
                is_match = False
                break
        result += 1 if is_match else 0
print(result)