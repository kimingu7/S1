def back(i,j):
    global sum_board, answer
    if answer < sum_board:
        return
    if i == n-1 and j == n-1:
        answer = sum_board
        return
    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= n or nj >= n:
            continue
        if not visited[ni][nj]:
            visited[ni][nj] = 1
            sum_board += board[ni][nj]
            back(ni,nj)
            sum_board -= board[ni][nj]
            visited[ni][nj] = 0

T = int(input())
di = [0,1]
dj = [1,0]
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    answer = 10000000
    sum_board = board[0][0]
    back(0,0)
    print(f'#{tc}',answer)