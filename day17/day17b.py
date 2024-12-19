"""Got stuck so found hint to look at outputs and check for periodicity (already tried it myself but only looked at first elements where there is no (obvious) periodicity)."""

with open('day17\\day17real.txt', 'r') as f:
    raw = f.read()

program = [int(i) for i in raw.split('\n')[-1].split(' ')[-1].split(',')]

A, B, C = -1, -1, -1

def get_combo_value(combo: int):
    if combo in [0, 1, 2, 3]:
        return combo
    elif combo == 4:
        return A
    elif combo == 5:
        return B
    elif combo == 6:
        return C
    else:
        return Exception

def check_output(output):
    return output[-1] == program[len(output) - 1]

def run_program():

    global A, B, C

    output = []

    pointer = 0

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

    return output


i = 8 ** 15 # this is where the outputs of correct length start and end at 8 ** 16 (can be calculated)
while True:
    A = i
    B = int(raw.split('\n')[1].split(' ')[-1])
    C = int(raw.split('\n')[2].split(' ')[-1])
    output = run_program()

    # use periodicity
    found = False
    for pos in range(16):
        if output[15 - pos] != program[15 - pos]:
            found = True
            # find first element from right that is incorrect and add according value of i to change it
            i += (8 ** (15 - pos))
            break
    if not found:
        print(i)
        break