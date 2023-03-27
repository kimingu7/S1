import sys
sys.setrecursionlimit(10**5)

def dfs(i,j):
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    visited[i][j] = 1
    color = paint[i][j]
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and paint[ni][nj] == color:
            if not visited[ni][nj]:
                dfs(ni,nj)


n = int(input())
paint = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
normal = 0
color_weak = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            normal+=1
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'R':
            paint[i][j] = 'G'
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            color_weak+=1
print(normal, color_weak)

# DFS, 혹은 BFS를 활용해서 푸는 문제
# 같은 값들이 연결되어있다면 한 구역, 다른 값이라면 다른 구역으로 생각
# dfs가 끝나면 연결된 구역에 대한 탐색이 끝났기 때문에 구역이 바뀐 것이므로 구역의 개수를 증가
# 3가지를 모두 구분하는 경우를 먼저 계산
# 적록색약의 경우 R과 G를 구분하지 못하기 때문에 하나로 바꿔준 뒤 계산
 