"""Already made it efficient in part A so no difference here except the number of steps."""

with open('day11\\day11real.txt', 'r') as f:
    raw = f.read()

numbers = [int(i) for i in raw.split(' ')]

lookup = {}

def get_count(x, steps_remaining):
    if steps_remaining == 0:
        return 1
    if (x, steps_remaining) in lookup:
        return lookup[(x, steps_remaining)]
    size = len(str(x))
    if x == 0:
        count = get_count(1, steps_remaining - 1)
    elif size % 2 == 0:
        a = int(str(x)[:size // 2])
        b = int(str(x)[size // 2:])
        count = get_count(a, steps_remaining - 1) + get_count(b, steps_remaining - 1)
    else:
        count = get_count(x * 2024, steps_remaining - 1)
    lookup[(x, steps_remaining)] = count
    return count

print(sum(get_count(x, 75) for x in numbers))