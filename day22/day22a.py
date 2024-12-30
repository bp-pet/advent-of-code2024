with open('day22\\day22real.txt', 'r') as f:
    raw = f.read()

numbers = [int(i) for i in raw.split('\n')]

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


result = 0
for x in numbers[:1]:
    for i in range(2000):
        x = get_next(x)
    result += x
print(result)