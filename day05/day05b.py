with open('day05\\day05real.txt', 'r') as f:
    raw = f.read()
    
from functools import cmp_to_key

temp = raw.split('\n\n')

rules_raw = temp[0]
rules = {}
for r in rules_raw.split('\n'):
    a = int(r.split('|')[0]) 
    b = int(r.split('|')[1])
    if b in rules:
        rules[b].add(a)
    else:
        rules[b] = set([a])

updates_raw = temp[1]
updates = []
for u in updates_raw.split('\n'):
    updates.append([int(i) for i in u.split(',')])

def compare(a, b):
    if a in rules and b in rules[a]:
        return 1
    if b in rules and a in rules[b]:
        return -1
    return 0

result = 0
for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(compare))
    if update != sorted_update:
        result += sorted_update[len(update)//2]

print(result)