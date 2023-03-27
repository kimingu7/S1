from collections import deque

t = 0
di = [0,0,1,-1]
dj = [1,-1,0,0]
while True:
    t+=1
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    theif = [[99999 for _ in range(n)] for _ in range(n)]
    q = deque([(0,0)])
    theif[0][0] = cave[0][0]
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if theif[ni][nj] > theif[i][j] + cave[ni][nj]:
                    theif[ni][nj] = theif[i][j] + cave[ni][nj]
                    q.append((ni,nj))
    answer = theif[n-1][n-1]
    print(f'Problem {t}: {answer}')

# 처음엔 단순히 최단경로로 갔을 때로 생각해 델타 방향을 (1,0)과 (0,1)로만 생각했음
# 근데 그건 최단경로로 갔을 때의 최소값을 구하는거라 문제에서 요구하는 답이 아님
# 따라서 모든 경우에 최소한으로 루피를 잃는 경로로 이동하게 해야함
# visited 배열을 만들어 다시 방문하지 않게 할 경우 최단 경로로 움직이게 됨
# 따라서 모든 칸에서 도달할 수 있는 각각의 경우의 수마다 최소값을 계산해야함