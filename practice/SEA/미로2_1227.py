from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]
n = 100

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        i, j = queue.popleft()
        if maze[i][j] == '0' or '2':
            maze[i][j] = '1'
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    if maze[ni][nj] == '0':
                        queue.append((ni,nj))
                    elif maze[ni][nj] == '3':
                        return 1
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                a, b = i, j
    print(f'#{tc} {bfs(a, b)}')