with open('day02\\day02real.txt', 'r') as f:
    raw = f.read()


result = 0
for report in raw.split('\n'):
    numbers = [int(i) for i in report.split(' ')]
    for i in range(len(report) + 1):
        numbers_filtered = numbers[0:i] + numbers[i + 1:]
        first_diff = numbers_filtered[1] - numbers_filtered[0]
        safe = True
        for i in range(len(numbers_filtered) - 1):
            diff = numbers_filtered[i + 1] - numbers_filtered[i]
            if first_diff * diff <= 0 or abs(diff) > 3:
                safe = False
                break
        if safe:
            result += 1
            break

print(result)