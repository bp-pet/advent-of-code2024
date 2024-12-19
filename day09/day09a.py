"""Was stuck til I got the hint that list cannot process as string because of multiple-digit numbers. That's obvious in hindsight but still example given was very misleading."""

with open('day09\\day09real.txt', 'r') as f:
    raw = f.read()


expanded = []
for i in range(len(raw)):
    expanded += int(raw[i]) * [i // 2] if i % 2 == 0 else int(raw[i]) * [-1]


left_marker = 0
right_marker = len(expanded) - 1
while left_marker < right_marker:
    if expanded[left_marker] != -1:
        left_marker += 1
        continue
    if expanded[right_marker] == -1:
        right_marker -= 1
        continue
    expanded[left_marker], expanded[right_marker] = expanded[right_marker], expanded[left_marker]
    left_marker += 1
    right_marker -= 1

checksum = sum(i * int(expanded[i]) if expanded[i] != -1 else 0 for i in range(len(expanded)))
print(checksum)