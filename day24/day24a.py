with open('day24\\day24real.txt', 'r') as f:
    raw = f.read()


#################### Check added later for part 2
    
def swap(a, b):
    global raw
    raw = raw.replace('> ' + a, 'temp')
    raw = raw.replace('> ' + b, '> ' + a)
    raw = raw.replace('temp', '> ' + b)

swap('ggn', 'z10')
swap('jcb', 'ndw')
swap('grm', 'z32')
swap('twr', 'z39')

x_bin = [0] * 45
y_bin = [0] * 45
for line in raw.split('\n\n')[0].split('\n'):
    if line[0] == 'x':
        x_bin[int(line[1:3])] = int(line[-1])
    if line[0] == 'y':
        y_bin[int(line[1:3])] = int(line[-1])


x_val = 0
for i, x in enumerate(x_bin):
    x_val += (2 ** i) * x
    
y_val = 0
for i, y in enumerate(y_bin):
    y_val += (2 ** i) * y

print(x_val + y_val)

###################

initial_vals = {}
for line in raw.split('\n\n')[0].split('\n'):
    initial_vals[line[:3]] = int(line[-1])

rules = {}
for line in raw.split('\n\n')[1].split('\n'):
    input1 = line.split(' ')[0]
    operator = line.split(' ')[1]
    input2 = line.split(' ')[2]
    output = line.split(' ')[4]
    rules[output] = (input1, operator, input2)

def get_value(x):
    if x in initial_vals:
        return initial_vals[x]
    rule = rules[x]
    input1 = get_value(rule[0])
    operator = rule[1]
    input2 = get_value(rule[2])
    if operator == 'AND':
        return input1 and input2
    elif operator == 'OR':
        return input1 or input2
    else:
        return input1 ^ input2


z_values = {}
for output in rules:
    if output[0] == 'z':
        z_values[output] = get_value(output)

result = 0
for i, z in enumerate(sorted(z_values)):
    result += (2 ** i) * z_values[z]
print(result)