import sys
n = int(sys.stdin.readline())
lst = [0 for _ in range(n)]
for i in range(n):
    lst[i] = int(sys.stdin.readline())
lst.sort()
for i in range(n):
    print(lst[i])