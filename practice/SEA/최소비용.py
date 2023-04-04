from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                temp = 1
                if graph[ni][nj] > graph[i][j]:
                    temp+=graph[ni][nj] - graph[i][j]
                if visited[ni][nj] > visited[i][j] + temp:
                    visited[ni][nj] = visited[i][j] + temp
                    q.append((ni,nj))

T = int(input())
INF = float('inf')
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    bfs()
    answer = visited[N-1][N-1]
    print(f'#{tc}',answer)
    
# bfs를 활용해 출발지에서 도착지까지 도달하는 최소 비용을 계산