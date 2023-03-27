from collections import deque

def bfs(i):
    global count
    q = deque([i])
    count = 0
    visited[i] = 1
    while q:
        i = q.popleft()
        for n in graph[i]:
            if not visited[n]:
                visited[n] = 1
                count+=1
                q.append(n)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = []
max_count = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    bfs(i)
    if max_count < count:
        max_count = count
        answer.clear()
        answer.append(i)
    elif max_count == count:
        answer.append(i)

print(*answer)

# 
# 
# 
# 