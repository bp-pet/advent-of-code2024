"""
Based fully on https://www.reddit.com/r/adventofcode/comments/1hnb969/2024_day_24_part_2_aliasing_wires_to_spot_the/. While I was trying to do it myself I didn't think the (fixed) sequence of gates had to be 1-to-1 with a ripple adder, so I didn't think about this way of solving it at all.
"""

with open('day24\\day24real.txt', 'r') as f:
    raw = f.read()


initial_vals = {}
rules = {}


def get_init_vals_and_rules():
    global initial_vals, rules
    initial_vals = {}
    rules = {}
    for line in raw.split('\n\n')[0].split('\n'):
        initial_vals[line[:3]] = int(line[-1])

    for line in raw.split('\n\n')[1].split('\n'):
        input1 = line.split(' ')[0]
        operator = line.split(' ')[1]
        input2 = line.split(' ')[2]
        output = line.split(' ')[4]
        rules[output] = (input1, operator, input2)

def swap(a, b):
    global raw
    raw = raw.replace('> ' + a, 'temp')
    raw = raw.replace('> ' + b, '> ' + a)
    raw = raw.replace('temp', '> ' + b)

def rate_rule(output):
    rule = rules[output]
    d1 = int(rule[0][-2:]) if rule[0][-2:].isdigit() else None
    d2 = int(rule[2][-2:]) if rule[2][-2:].isdigit() else None
    if d1 is not None and d2 is not None:
        return (d1 + d2) / 2
    if d1 is not None:
        return d1
    if d2 is not None:
        return d2
    return 1000


swap('ggn', 'z10')
swap('jcb', 'ndw')
swap('grm', 'z32')
swap('twr', 'z39')
get_init_vals_and_rules()

def rename(old, new):
    global raw
    raw = raw.replace(old, new)
    get_init_vals_and_rules()

def get_prev_index(index):
    return str(int(index) - 1).zfill(2)

# rename first gates
input_bit_indices = []
for output in rules:
    if rules[output][0][0] in ['x', 'y']:
        input_bit_indices.append(rules[output][2][1:]) # saving for later use
        assert rules[output][0][1:] == rules[output][2][1:]
        rename(output, rules[output][1] + rules[output][0][1:])
input_bit_indices = sorted(list(set(input_bit_indices)))


# rename rest
rename('AND00', 'CARRY00')
for index in input_bit_indices[1:]:
    
    # XOR01 AND CARRY00 -> CARRY_INTERMEDIATE01
    for output in rules:
        required_inputs = ['XOR' + index, 'CARRY' + get_prev_index(index)]
        if rules[output][1] == 'AND' and rules[output][0] in required_inputs and rules[output][2] in required_inputs:
            rename(output, 'CARRY_INTERMEDIATE' + index)
    
    # AND01 OR CARRY_INTERMEDIATE01 -> CARRY01
    for output in rules:
        required_inputs = ['AND' + index, 'CARRY_INTERMEDIATE' + index]
        if rules[output][1] == 'OR' and rules[output][0] in required_inputs and rules[output][2] in required_inputs:
            rename(output, 'CARRY' + index)

# check manually where it goes wrong
# for output in sorted(rules, key=rate_rule):
#     print(output, rules[output])

# swaps done earlier in script
result = ['ggn', 'z10', 'jcb', 'ndw', 'grm', 'z32', 'twr', 'z39']
print(','.join(sorted(result)))