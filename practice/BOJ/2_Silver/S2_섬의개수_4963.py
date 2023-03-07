import sys
sys.setrecursionlimit(10**5)
di = [1, 1, 1, 0, 0, -1, -1, -1]
dj = [1, 0, -1, 1, -1, 1, 0, -1]

def DFS(i, j):
    map_[i][j] = 0
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < h and 0 <= nj < w and map_[ni][nj] == 1:
            DFS(ni, nj)

while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    map_ = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0
    for i in range(h):
        map_.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and map_[i][j] == 1:
                DFS(i, j)
                cnt+=1
    print(cnt)

# 델타검색을 활용한 DFS 문제
# 기본적인 알고리즘은 연결요소의 개수를 구하는 것과 같음
# 이 문제에서는 대각선 방향으로 이어져있어도 연결되어있는 것으로 판단함
# 따라서 8방향으로 델타검색을 진행함