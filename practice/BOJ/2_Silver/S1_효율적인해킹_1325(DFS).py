import sys
sys.setrecursionlimit(10**6)

def dfs(s):
    global count
    for i in graph[s]:
        if not visited[i]:
            visited[i] = 1
            count+=1
            dfs(i)
    

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
hacking_count = [0 for _ in range(n+1)]
max_count = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
for k in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    count = 0
    dfs(k)
    hacking_count[k] = count
    if max_count < count:
        max_count = count
for i in range(len(hacking_count)):
    if hacking_count[i] == max_count:
        print(i,end=' ')

# dfs로 풀었는데 왜 시간초과가 뜨는지 모르겠음
# bfs로 풀어야할거 같은 느낌