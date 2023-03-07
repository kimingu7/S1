from collections import deque

def island(i,j):
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and sea[ni][nj]:
                visited[ni][nj] = 1
                sea[ni][nj] = island_num
                q.append((ni,nj))

def bridge(s):
    que = deque()
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if sea[i][j] == s:
                distance[i][j] = 0
                que.append((i,j))
    
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if sea[ni][nj] and sea[ni][nj] != s:
                    return distance[i][j]
                elif (not sea[ni][nj]) and distance[ni][nj] == -1:
                    distance[ni][nj] = distance[i][j] + 1
                    que.append((ni,nj))
    return int(1e9)


di = [1,-1,0,0]
dj = [0,0,1,-1]
n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]
island_num = 1
visited = [[0 for _ in range(n)] for _ in range(n)]
result = 1e9
for i in range(n):
    for j in range(n):
        if sea[i][j] and not visited[i][j]:
            visited[i][j] = 1
            sea[i][j] = island_num
            island(i,j)
            island_num+=1
for s in range(1,island_num):
    result = min(result, bridge(s))
print(result)

# bfs를 두번 돌려야 하는 문제
# 첫번째 bfs(island)에서는 섬마다 넘버링을 해줌
# 두번째 bfs(bridge)에서는 섬과 섬 사이의 거리를 distance 배열에 저장