T = int(input())

di = [1,1,1,0]
dj = [0,1,-1,1]

for tc in range(1,T+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    ans = 'NO'
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'o':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 'o':
                        cnt = 1
                        for s in range(1,5):
                            si = i + di[k] * s
                            sj = j + dj[k] * s
                            if 0 <= si < n and 0 <= sj < n:
                                if board[si][sj] == 'o':
                                    cnt+=1
                                else :
                                    cnt = 0
                        if cnt >= 5:
                            ans = 'YES'
                            break
    print(f'#{tc}', ans)

# 델타탐색을 응용하여 푸는 문제