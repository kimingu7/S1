import sys
n, m = map(int, sys.stdin.readline().split())
d = set()
b = set()
dbj = []
for i in range(n):
    d.add(input())
for i in range(m):
    b.add(input())
dbj = sorted(list(d&b))
print(len(dbj))
for i in dbj:
    print(i)