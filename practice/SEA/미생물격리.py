T = int(input())

dr = (0,-1,1,0,0)
dc = (0,0,0,-1,1)
rev = (0,2,1,4,3)

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    board = []
    for _ in range(k):
        board.append(list(map(int, input().split())))
    for _ in range(m):
        info = dict()
        for row in range(k):
            r,c,l,d = board[row]
            if not l:
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            board[row][0], board[row][1] = nr, nc
            if not (1 <= nr < n-1 and 1 <= nc < n-1):
                board[row][2] //= 2
                board[row][3] = rev[d]
            if (nr, nc) not in info.keys():
                info[(nr, nc)] = [row, l]
            else :
                num, size = info[(nr,nc)]
                if board[row][2] > size:
                    info[(nr, nc)] = [row, board[row][2]]
                    board[row][2] += board[num][2]
                    board[num][2] = 0
                else :
                    board[num][2] += board[row][2]
                    board[row][2] = 0
    answer = 0
    for b in board:
        answer += b[2]
    print(f'#{tc}',answer)