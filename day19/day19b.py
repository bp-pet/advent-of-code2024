with open('day19real.txt', 'r') as f:
    raw = f.read()

patterns = raw.split('\n\n')[0].split(', ')
designs = raw.split('\n\n')[1].split('\n')

lookup = {}

def has_options(design):
    if design in lookup:
        return lookup[design]
    count = 0
    for pattern in patterns:
        length = len(pattern)
        if pattern == design[:length]:
            if len(design) == len(pattern):
                count += 1
            else:
                count += has_options(design[length:])
    lookup[design] = count
    return count


result = 0
for design in designs:
    result += has_options(design)
print(result)