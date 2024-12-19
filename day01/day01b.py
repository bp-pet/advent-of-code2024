with open('day01\\day01real.txt') as f:
    raw = f.read()

list1 = []
list2 = []

for line in raw.split('\n'):
    list1.append(int(line.split(' ')[0]))
    list2.append(int(line.split(' ')[3]))

result = 0
for i in list1:
    counter = 0
    for j in list2:
        counter += 1 if i == j else 0
    result += i * counter

print(result)