import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
sums = [0]
tmp = 0
for a in lst:
    tmp += a
    sums.append(tmp)
for a in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sums[j] - sums[i-1])