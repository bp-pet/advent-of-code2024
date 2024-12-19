with open('day07\\day07real.txt', 'r') as f:
    raw = f.read()


equations = []
for eq_raw in raw.split('\n'):
    eq_left = int(eq_raw.split(':')[0])
    eq_right = [int(i) for i in eq_raw.split(' ')[1:]]
    equations.append({'left': eq_left, 'right': eq_right})


def concatenate_numbers(a, b):
    return int(str(a) + str(b))


def check_equation(current_value, target_value, remaining_numbers):
    if current_value > target_value:
        return False
    if remaining_numbers == []:
        return current_value == target_value
    return check_equation(current_value + remaining_numbers[0], target_value, remaining_numbers[1:]) or check_equation(current_value * remaining_numbers[0], target_value, remaining_numbers[1:]) or check_equation(concatenate_numbers(current_value,remaining_numbers[0]), target_value, remaining_numbers[1:])

result = 0
for eq in equations:
    if check_equation(eq['right'][0], eq['left'], eq['right'][1:]):
        result += eq['left']

print(result)