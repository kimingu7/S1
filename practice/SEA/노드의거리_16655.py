from collections import deque

def bfs(start, end):
    visited = [0 for _ in range(v+1)]
    queue = deque()
    queue.append((start,0))
    while queue:
        n, depth = queue.popleft()
        if not visited[n]:
            visited[n] = 1
        for k in graph[n]:
            if not visited[k]:
                if k == end:
                    return depth+1
                else :
                    visited[k] = 1
                    queue.append((k, depth+1))
    return 0

T = int(input())
for tc in range(1,T+1):
    v, e = map(int, input().split())
    graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
    for i in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    s, g = map(int, input().split())
    print(f'#{tc} {bfs(s,g)}')

# BFS를 활용해 그래프경로 문제의 깊이를 구하는 문제
# 그래프의 형태를 수정했음
# 깊이를 재기 위해 queue를 시작점 start와 깊이 0으로 시작
# 시작점 n의 visited[n] = 1
# 방문하지 않은 노드 k가 도착점 end가 아닐 경우 visited[k] = 1, cnt에 1을 더해 bfs 진행
# 방문하지 않은 노드 k가 도착점 end일 경우 cnt에 1을 더해 반환
# queue가 비었다면(모든 노드를 탐색했다면) 0 반환