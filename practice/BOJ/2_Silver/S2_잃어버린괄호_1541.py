n = int(input())
t = int(input())
graph = [[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

def dfs(t):
    visited[t]=1
    for i in graph[t]:
        if visited[i]==0:
            dfs(i)

for i in range(t):
    a, b = map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]

dfs(1)
print(sum(visited)-1)