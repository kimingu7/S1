def back(i, j):
    global rst
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    if maze[i][j] == 3:
        rst = 1
    else :
        maze[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] != 1:
                    back(ni, nj)

t = int(input())
for i in range(t):
    rst = 0
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    for j in range(n):
        for k in range(n):
            maze[j][k] = int(maze[j][k])
            if maze[j][k] == 2:
                a, b = j, k
    back(a, b)
    print(f'#{i+1} {rst}')

# 백트래킹을 활용해 미로찾기를 하는 문제
# maze 행렬을 int 형태로 입력받을 경우 0이 사라지는 문제가 있어 문자열로 받은 뒤 int 형태로 다시 변경해줬음
# 근데 지금 생각해보니 그냥 변환 안하고 문자열로 해결해도 됐을듯
# back 함수 안에서 목표인 3에 도착했을 때 rst 값은 1 (기본 값 0)
# 델타검색을 응용해 인접한 4칸 중 이동할 수 있는 칸으로 연속해서 이동했음
# 이미 이동한 칸으로 다시 가지 않기 위해 이미 지나온 칸은 1로 바꿔줌
# 시작점인 2의 (a, b)를 구해 back(a, b) 실행시킨 뒤 rst 값 출력