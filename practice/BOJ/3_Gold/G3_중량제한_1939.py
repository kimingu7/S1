import sys
from collections import deque

def bfs(mid):
    visited[f1] = 1
    queue = deque()
    queue.append(f1)
    while queue:
        x = queue.popleft()
        if x == f2:
            return True
        for nx, nc in bridge[x]:
            if visited[nx] == 0 and mid <= nc:
                queue.append(nx)
                visited[nx] = 1
    return False

n, m = map(int, input().split())
bridge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append((b,c))
    bridge[b].append((a,c))
for i in range(1,n+1):
    bridge[i].sort(reverse=True)
f1, f2 = map(int, input().split())
l, h = 1, 1000000000
while l <= h:
    visited = [0 for _ in range(n+1)]
    mid = (l + h) // 2
    if bfs(mid):
        l = mid + 1
    else :
        h = mid - 1
print(h)

# 이분 탐색과 bfs를 동시에 진행