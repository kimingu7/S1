import sys
input = sys.stdin.readline

def check():
    for start in range(n):
        k = start # k는 이동하는 가로선
        for j in range(h):
            if board[j][k]: # 가로선이 오른쪽에 존재할 때 오른쪽으로 이동
                k+=1
            elif k > 0 and board[j][k-1]: # 왼쪽에 존재한다면 왼쪽으로 이동
                k-=1
        if k != start: # 가장 하단까지 왔을 때 k와 start가 같지 않다면 False
            return False
    return True

def dfs(cnt, x, y):
    global result
    if check():
        result = min(result, cnt)
        return
    elif cnt == 3 or result <= cnt:
        return
    for i in range(x, h):
        if i == x: # 행이 변경되기 전엔 가로선을 계속해 탐색
            k = y
        else : # 행이 변경될 경우 처음부터 탐색
            k = 0
        for j in range(k, n-1):
            if not board[i][j] and not board[i][j+1]: # 가로선을 놨을 때 오른쪽에 존재하지 않아야함
                if j > 0 and board[i][j-1]: # 가로선을 놨을 때 왼쪽에 존재할 경우 continue
                    continue
                board[i][j] = True # 가로선 놓기
                dfs(cnt+1, i, j+2) # 가로선을 놨기 때문에 cnt 1 증가, 가로선은 2 증가
                board[i][j] = False # 가로선 없애기

n, m, h = map(int, input().split())
board = [[False for _ in range(n)] for _ in range(h)] # 방문한 지점 체크
if m == 0: # M이 0일 경우 계산할 필요가 없으므로 0을 출력하고 종료
    print(0)
    exit()
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = True
result = 4
dfs(0,0,0)
if result < 4:
    answer = result
else :
    answer = -1
print(answer)