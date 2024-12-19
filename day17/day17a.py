with open('day17\\day17real.txt', 'r') as f:
    raw = f.read()

A = int(raw.split('\n')[0].split(' ')[-1])
B = int(raw.split('\n')[1].split(' ')[-1])
C = int(raw.split('\n')[2].split(' ')[-1])

program = [int(i) for i in raw.split('\n')[-1].split(' ')[-1].split(',')]

pointer = 0

def get_combo_value(combo: int):
    if combo in [1, 2, 3]:
        return combo
    elif combo == 4:
        return A
    elif combo == 5:
        return B
    elif combo == 6:
        return C
    else:
        return Exception

output = []

while True:
    if pointer > len(program) - 1:
        break
    opcode = program[pointer]
    operand = program[pointer + 1]

    if opcode == 0:
        A = A // (2 ** get_combo_value(operand))
    elif opcode == 1:
        B = B ^ operand
    elif opcode == 2:
        B = get_combo_value(operand) % 8
    elif opcode == 3:
        if A != 0:
            pointer = operand - 2
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        output.append(get_combo_value(operand) % 8)
    elif opcode == 6:
        B = A // (2 ** get_combo_value(operand))
    elif opcode == 7:
        C = A // (2 ** get_combo_value(operand))
    else:
        raise Exception
    
    pointer += 2

result = ','.join([str(i) for i in output])

print(result)