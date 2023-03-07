import sys
n = int(sys.stdin.readline())
dot = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    dot[i] = list(map(int,sys.stdin.readline().split()))
dot = sorted(dot, key=lambda x:x[1])
dot = sorted(dot, key=lambda x:x[0])
for i in dot:
    print(*i)