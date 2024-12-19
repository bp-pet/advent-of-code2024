with open('day19real.txt', 'r') as f:
    raw = f.read()

patterns = raw.split('\n\n')[0].split(', ')
designs = raw.split('\n\n')[1].split('\n')


def has_options(design):
    for pattern in patterns:
        length = len(pattern)
        if pattern == design[:length]:
            if len(design) == len(pattern):
                return True
            else:
                if has_options(design[length:]):
                    return True
    return False


result = 0
for design in designs:
    result += has_options(design)
print(result)