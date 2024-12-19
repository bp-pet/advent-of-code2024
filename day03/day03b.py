with open('day03\\day03real.txt', 'r') as f:
    raw = f.read()

import re

result = 0

for i, part in enumerate(raw.split('don\'t()')): # split on don't
    if i != 0: # for first one always take everything
        if 'do()' in part:
            part = ''.join(part.split('do()')[1:]) # take everything after first do
        else:
            part = '' # if no do then ignore part

    for match in re.findall(r'mul\(\d+,\d+\)', part):
        d1 = match.split('(')[1].split(',')[0]
        d2 = match.split(',')[1].split(')')[0]
        result += int(d1) * int(d2)
print(result)