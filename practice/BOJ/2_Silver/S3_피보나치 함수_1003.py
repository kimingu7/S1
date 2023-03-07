f0 = [1, 0, 1]
f1 = [0, 1, 1]
def f(n):
    lgt = len(f0)
    if n >= lgt:
        for i in range(lgt, n+1):
            f0.append(f0[i-1]+f0[i-2])
            f1.append(f1[i-1]+f1[i-2])
    print(f'{f0[n]} {f1[n]}')
t = int(input())
for i in range(t):
    n = int(input())
    f(n)