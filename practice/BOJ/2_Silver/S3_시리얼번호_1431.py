n = int(input())
serial = []

def sum_serial(num):
    result = 0
    for n in num:
        if n.isdigit():
            result+=int(n)
    return result 

for _ in range(n):
    serial.append(input())

serial.sort(key = lambda x:(len(x), sum_serial(x), x))
for s in serial:
    print(s)