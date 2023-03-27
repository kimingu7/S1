import sys
t = int(input())
for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    if a > b :
        n = b
        m = a
    else :
        n = a
        m = b
    for i in range(n,0,-1):
        if a % i == 0 and b % i == 0:
            print((a//i)*(b//i)*i)
            break