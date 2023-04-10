from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if mountain[ni][nj] < mountain[i][j]:
                    tmp = visited[i][j]
                elif mountain[ni][nj] > mountain[i][j]:
                    tmp = visited[i][j] + (abs(mountain[ni][nj] - mountain[i][j])*2)
                else :
                    tmp = visited[i][j] + 1
                if tmp < visited[ni][nj]:
                    visited[ni][nj] = tmp
                    q.append((ni,nj))

T = int(input())
INF = 1e9
for tc in range(1,T+1):
    N = int(input())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF for _ in range(N)] for _ in range(N)]
    bfs()
    print(f'#{tc}',visited[N-1][N-1])