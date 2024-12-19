"""The checksum calculation can be sped up a lot by calculating the sum for each instead of iterating. In my original solution (on another laptop) I implemented that, thinking it was necessary. But it turned out I had a different mistake there. So I didn't bother implementing it here."""

with open('day09\\day09real.txt', 'r') as f:
    raw = f.read()


expanded = []
for i in range(len(raw)):
    expanded.append((int(raw[i]), i // 2) if i % 2 == 0 else (int(raw[i]), -1))

right_marker = len(expanded) - 1

def visualize_batch():
    """For debugging only"""
    result = ''
    for x in expanded:
        if x[1] == -1:
            result += '.' * x[0]
        else:
            result += str(x[1]) * x[0]
    return result


while right_marker > 0:
    if expanded[right_marker][1] == -1:
        right_marker -= 1
        continue
    left_marker = 0
    while left_marker < right_marker:
        if expanded[left_marker][1] != -1 or expanded[left_marker][0] < expanded[right_marker][0]:
            left_marker += 1
            continue
        temp_right = expanded[right_marker]
        diff = expanded[left_marker][0] - expanded[right_marker][0]
        expanded[right_marker] = (temp_right[0], -1)
        expanded[left_marker] = temp_right
        expanded.insert(left_marker + 1, (diff, -1))
        right_marker += 1
        break
    right_marker -= 1

counter = 0
checksum = 0
for t in expanded:
    for i in range(t[0]):
        if t[1] != -1:
            checksum += counter * t[1]
        counter += 1
print(checksum)