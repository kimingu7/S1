from collections import deque

n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, input())))

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs(i,j):
    q = deque()
    q.append((i,j))

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= n or ni < 0 or nj >= m or nj < 0:
                continue
            if maze[ni][nj] == 0:
                continue
            if maze[ni][nj] == 1:
                maze[ni][nj] = maze[i][j] + 1
                q.append((ni,nj))
bfs(0,0)
print(maze[n-1][m-1])

# bfs와 델타탐색을 활용해 한칸씩 탐색하며 최소 경로로 도착점에 도달하는 경우를 구함
# 미로의 칸이 0일 때는 continue
# 미로의 칸이 1일 때는 이전 칸에 1을 더해서 깊이를 계산
# 미로의 칸이 그 이외일 경우는 이미 지나온 길이기 때문에 계산하지 않음