with open('day03\\day03real.txt', 'r') as f:
    raw = f.read()

import re

result = 0
for match in re.findall(r'mul\(\d+,\d+\)', raw):
    d1 = match.split('(')[1].split(',')[0]
    d2 = match.split(',')[1].split(')')[0]
    result += int(d1) * int(d2)
print(result)