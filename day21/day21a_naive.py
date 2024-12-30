"""
To decide which path between buttons to take, take essentially a random feasible one. This doesn't give the shortest sequence for one of the examples.
"""
# Step 1: record paths between buttons

import numpy as np

numpad_layout = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']])
dpad_layout = np.array([[None, 'U', 'A'], ['L', 'D', 'R']])

numpad_sequences = {}
for i in range(numpad_layout.shape[0]):
    for j in range(numpad_layout.shape[1]):
        start_pos = (i, j)
        if numpad_layout[start_pos] is None:
            continue
        for k in range(numpad_layout.shape[0]):
            for l in range(numpad_layout.shape[1]):
                end_pos = (k, l)
                if numpad_layout[end_pos] is None:
                    continue
                sequence = ''
                
                # always move up and/or right first to avoid going over empty spot
                if start_pos[0] > end_pos[0]:
                    for _ in range(start_pos[0] - end_pos[0]):
                        sequence += 'U'
                if start_pos[1] <= end_pos[1]:
                    for _ in range(end_pos[1] - start_pos[1]):
                        sequence += 'R'
                if start_pos[0] <= end_pos[0]:
                    for _ in range(end_pos[0] - start_pos[0]):
                        sequence += 'D'
                if start_pos[1] > end_pos[1]:
                    for _ in range(start_pos[1] - end_pos[1]):
                        sequence += 'L'
                sequence += 'A'
                numpad_sequences[numpad_layout[start_pos] + numpad_layout[end_pos]] = sequence


dpad_sequences = {}
for i in range(dpad_layout.shape[0]):
    for j in range(dpad_layout.shape[1]):
        start_pos = (i, j)
        if dpad_layout[start_pos] is None:
            continue
        for k in range(dpad_layout.shape[0]):
            for l in range(dpad_layout.shape[1]):
                end_pos = (k, l)
                if dpad_layout[end_pos] is None:
                    continue
                sequence = ''
                
                # always move down and/or right first to avoid going over empty spot
                if start_pos[1] <= end_pos[1]:
                    for _ in range(end_pos[1] - start_pos[1]):
                        sequence += 'R'
                if start_pos[0] <= end_pos[0]:
                    for _ in range(end_pos[0] - start_pos[0]):
                        sequence += 'D'
                if start_pos[0] > end_pos[0]:
                    for _ in range(start_pos[0] - end_pos[0]):
                        sequence += 'U'
                if start_pos[1] > end_pos[1]:
                    for _ in range(start_pos[1] - end_pos[1]):
                        sequence += 'L'
                sequence += 'A'
                dpad_sequences[dpad_layout[start_pos] + dpad_layout[end_pos]] = sequence


# Step 2: perform everything

class Pad:
    def __init__(self, pad_type: str):
        self.current_position = 'A'
        if pad_type == 'num':
            self.sequences = numpad_sequences
        elif pad_type == 'dir':
            self.sequences = dpad_sequences
        else:
            raise Exception('Type of pad not implemented')
    
    def press_key(self, key_to_press):
        """Returns the sequence of keys needed to get to new state (and press it) and sets new state."""
        sequence_key = self.current_position + key_to_press
        self.current_position = key_to_press
        try:
            return self.sequences[sequence_key]
        except KeyError:
            raise Exception('Something is wrong')

numpad = Pad('num')
dpad1 = Pad('dir')
dpad2 = Pad('dir')

with open('day21\\day21example.txt', 'r') as f:
    raw = f.read()
passwords = raw.split('\n')

result = 0
for password in passwords:
    required_sequence = ''
    for c0 in password:
        for c1 in numpad.press_key(c0):
            for c2 in dpad1.press_key(c1):
                required_sequence += dpad2.press_key(c2)
    result += len(required_sequence) * int(password[:-1])
print(result)