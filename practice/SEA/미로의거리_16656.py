from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs(i,j):
    visited = [[0 for _ in range(n)] for _ in range(n)]
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
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append((ni,nj))
                    elif maze[ni][nj] == '3':
                        return visited[i][j]
    return 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                a, b = i, j
    print(f'#{tc} {bfs(a, b)}')


# BFS를 활용해 미로의 최단거리를 찾는 문제
# maze 행렬을 int 형태로 입력받을 경우 0이 사라지는 문제가 있어 문자열로 받음
# 델타검색을 응용해 인접한 4칸 중 이동할 수 있는 칸으로 연속해서 이동했음
# 이미 이동한 칸으로 다시 가지 않기 위해 이미 지나온 칸은 1로 바꿔줌
# visited 배열을 만들어 방문하는 칸마다 1씩 증가시킴(이동한 거리를 의미)
# bfs 함수 안에서 목표인 3에 도착했을 때 총 이동한 거리 visited[i][j]를 반환
# 도착하지 못했을 경우 0 반환
# 시작점인 2의 (a, b)를 구해 bfs(a, b) 실행시킨 뒤 return 값 출력