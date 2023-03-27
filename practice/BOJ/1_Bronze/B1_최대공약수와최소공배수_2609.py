a, b = map(int, input().split())
if a > b :
    n = b
    m = a
else :
    n = a
    m = b
for i in range(n,0,-1):
    if a % i == 0 and b % i == 0:
        print(i)
        print((a//i)*(b//i)*i)
        break