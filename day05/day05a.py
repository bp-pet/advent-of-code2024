with open('day05\\day05real.txt', 'r') as f:
    raw = f.read()


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
    updates.append(tuple([int(i) for i in u.split(',')]))


result = 0
for update in updates:
    invalid = False
    for i in range(len(update)):
        if update[i] not in rules:
            continue
        if set(update[i+1:]) & rules[update[i]]:
            invalid = True
            break
    if not invalid:
        result += update[i//2]


print(result)