def DFS(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i] = visited[s]+1
            DFS(i)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 1
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

DFS(a)
if visited[b] > 0:
    print(visited[b])
else :
    print(-1)

# DFS를 활용해 촌수를 계산하는 문제
# 탐색을 진행하며 직접 연결된 노드에 1을 더해주는 것이 핵심
# visited[b]가 존재할 경우 visited[b]를 출력하고
# 존재하지 않을 경우 -1을 출력해줌