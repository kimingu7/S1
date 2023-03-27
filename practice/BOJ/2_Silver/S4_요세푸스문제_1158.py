from collections import deque
n, k = map(int, input().split())
d = deque()
for i in range(1, n+1):
    d.append(i)
print('<', end='')
while d:
    for i in range(k-1):
        d.append(d[0])
        d.popleft()
    print(d.popleft(), end='')
    if d:
        print(', ', end='')
print('>')