def DFS(s, d):
    visited[s] = 1
    for i in graph[s]:
        if not visited[i]:
            DFS(i, d+1)

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            cnt+=1
            visited[i] = 1
        else :
            DFS(i,0)
            cnt+=1
print(cnt)

# 연결요소의 개수를 DFS 방식으로 풀었을 때
# 방문하지 않았으면서 연결되지 않은 경우(고립된 경우) cnt 1 증가
# 방문하지 않았으면서 연결된 DFS 탐색
# 한번 탐색을 끝낼 때마다 cnt를 1씩 증가