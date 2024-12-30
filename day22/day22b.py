import numpy as np
import itertools

with open('day22\\day22real.txt', 'r') as f:
    raw = f.read()

input_numbers = [int(i) for i in raw.split('\n')]

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def get_next(number):
    temp = number * 64
    number = mix(number, temp)
    number = prune(number)

    temp = number // 32
    number = mix(number, temp)
    number = prune(number)
    
    temp = number * 2048
    number = mix(number, temp)
    number = prune(number)

    return number


prices_all = []
changes_all = []
for x in input_numbers:
    prices = []
    changes = []
    for _ in range(2001):
        value = x % 10
        if len(prices) > 0:
            changes.append(value - prices[-1])
        prices.append(value)
        x = get_next(x)
    prices_all.append(prices)
    changes_all.append(changes)


sequence_values = np.full((19, 19, 19, 19), 0)
for index, prices in enumerate(prices_all):
    sequence_found = np.full((19, 19, 19, 19), False)
    for i in range(4, len(prices)):
        sequence = tuple(changes_all[index][i - 4:i])
        coords = tuple(np.array(sequence) + np.array((9, 9, 9, 9)))
        if not sequence_found[coords]:
            sequence_values[coords] += prices[i]
            sequence_found[coords] = True


max_profit = 0
max_pattern = None
for pattern in itertools.product(range(19), repeat=4):
    profit = sequence_values[pattern]
    if profit > max_profit:
        max_profit = profit
        max_pattern = tuple(np.array(pattern) - np.array((9, 9, 9, 9)))

print(max_pattern, max_profit)