from collections import deque
T = int(input())
 
di = [1,-1,0,0]
dj = [0,0,1,-1]
def bfs():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if visited[ni][nj] != -1:
                continue
            q.append((ni,nj))
            visited[ni][nj] = visited[i][j] + 1
 
for tc in range(1,T+1):
    n, m = map(int, input().split())
    waterpark = []
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    for i in range(n):
        temp = input()
        for j in range(m):
            if temp[j] == 'W':
                q.append((i,j))
                visited[i][j] = 0
    bfs()
    result = 0
    for i in range(n):
        for j in range(m):
            result+=visited[i][j]
    print(f'#{tc}', result)

# bfs를 통해 W에서 모든 L로 갈 수 있는 최단 거리를 구함
# visited 배열을 -1로 초기화해야함