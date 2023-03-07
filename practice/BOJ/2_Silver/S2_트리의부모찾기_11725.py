from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        n = queue.pop()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                answer[i] = n
                queue.append(i)


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs()
for i in range(2,n+1):
    print(answer[i])

# 루트가 1인 트리에서 1을 제외한 각 노드의 부모 노드를 찾는 문제
# bfs 또는 dfs를 이용해 풀 수 있음
# 연결되어있고 방문하지 않은 배열이면 visited 배열을 1로 초기화하고, answer 배열에는 n을 저장(n은 직전 노드)