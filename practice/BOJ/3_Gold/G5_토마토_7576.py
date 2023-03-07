import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((0,i,j))
while queue:
    date, x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = 1
            queue.append((date+1, nx, ny))
for i in range(n):
    if 0 in box[i]:
        print(-1)
        sys.exit()
print(date)