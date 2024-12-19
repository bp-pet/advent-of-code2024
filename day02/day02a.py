with open('day02\\day02real.txt', 'r') as f:
    raw = f.read()


result = 0
for report in raw.split('\n'):
    numbers = [int(i) for i in report.split(' ')]
    first_diff = numbers[1] - numbers[0]
    safe = True
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if first_diff * diff <= 0 or abs(diff) > 3:
            safe = False
            break
    if safe:
        result += 1

print(result)