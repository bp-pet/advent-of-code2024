with open('day01\\day01real.txt') as f:
    raw = f.read()

list1 = []
list2 = []

for line in raw.split('\n'):
    list1.append(int(line.split(' ')[0]))
    list2.append(int(line.split(' ')[3]))

list1.sort()
list2.sort()


result = 0
for i in range(len(list1)):
    result += abs(list1[i] - list2[i])

print(result)