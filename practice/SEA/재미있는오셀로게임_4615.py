def othello(i,j,color):
    di = [1,1,1,0,0,-1,-1,-1]
    dj = [1,0,-1,1,-1,1,0,-1]
    if not board[i][j]:
        board[i][j] = color
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            stack = []
            while True:
                if ni < 0 or n <= ni or nj < 0 or n <= nj:
                    stack.clear()
                    break
                if board[ni][nj] == 0:
                    stack.clear()
                    break
                if board[ni][nj] == color:
                    break
                else :
                    stack.append((ni,nj))
                ni+=di[k]
                nj+=dj[k]
            for ki, kj in stack:
                board[ki][kj] = color
 
t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[n//2-1][n//2] = board[n//2][n//2-1] = 1
    board[n//2-1][n//2-1] = board[n//2][n//2] = 2
    W = B = 0
    for _ in range(m):
        j, i, color = map(int, input().split())
        a, b = i-1, j-1
        othello(a, b, color)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                B+=1
            elif board[i][j] == 2 :
                W+=1
    print(f'#{tc} {B} {W}')

# 맨 처음 돌 두는 자리를 매우 조심해서 둬야함
# 8방향 델타검색을 기초로 함
# line 10 델타검색의 범위가 board를 넘어설 경우 스택을 비우고 break
# line 13 0을 만나게 되면 스택을 비우고 break
# line 16 같은 color를 만나게 되면 break
# line 18 else의 경우 다른 color를 만나는 경우의 수이므로 stack에 다른 color(뒤집어야할 칸)의 좌표를 append
# line 20, 21 di[k], dj[k] 방향으로 쭉 나아가면서 탐색
# line 22 뒤집어야할 칸은 stack에 좌표가 있으므로 color로 바꿔줌