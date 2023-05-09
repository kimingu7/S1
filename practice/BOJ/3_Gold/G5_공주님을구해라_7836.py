from collections import deque

n, m, t = map(int, input().split())

di = [1,-1,0,0]
dj = [0,0,1,-1]

castle = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if castle[i][j] == 2:
            gi = i
            gj = j

visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        si, sj = q.popleft()
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and castle[ni][nj] != 1:
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[si][sj] + 1
                    q.append((ni,nj))

bfs()

t1 = visited[n-1][m-1]
t2 = abs(n-1-gi) + abs(m-1-gj) + visited[gi][gj]

if visited[gi][gj] == 0:
    answer = t1
elif t1 == 0 and n != 1 and m != 1:
    answer = t2
else :
    answer = min(t1, t2)

if n == 1 and m == 1:
    print(0)
elif 0 < answer <= t:
    print(answer)
elif answer > t or answer == 0:
    print('Fail')