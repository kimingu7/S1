T = int(input())
way = [(0,-1),(-1,0),(0,1),(1,0)]
tunnel_type = [[],[0,1,2,3],[1,3],[0,2],[1,2],[3,2],[3,0],[1,0]]
def bfs(n,m):
    while q:
        i, j = q.pop(0)
        ways = tunnel_type[tunnel[i][j]]
        if ways == []:
            continue
        for k in ways:
            di, dj = way[k]
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and tunnel[ni][nj] != 0:
                criminal = tunnel_type[tunnel[ni][nj]]
                for l in criminal:
                    mi, mj = ni + way[l][0], nj + way[l][1]
                    if mi == i and mj == j:
                        q.append((ni,nj))
                        visited[ni][nj] = visited[i][j] + 1



for tc in range(1,T+1):
    n,m,r,c,l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[r][c] = 1
    q = [(r,c)]
    bfs(n,m)
    count = 0
    for i in range(n):
        for j in range(m):
            if 0 < visited[i][j] <= l:
                count+=1
    print(f'#{tc}',count)

# 주어진 터널의 정보에 따라 연결 여부를 파악해야하는 문제
# 움직이는 경로를 bfs를 통해 구하고, visited 배열의 값이 l 이하인 경우만 count
# 
# 