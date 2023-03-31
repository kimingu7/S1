def back(i,j,tmp,cnt):
    global numbers
    if cnt == 7:
        numbers.add(tmp)
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= 4 or ni < 0 or nj >= 4 or nj < 0:
            continue
        else :
            tmp += board[ni][nj] * (10 ** cnt)
            back(ni, nj, tmp, cnt+1)
            tmp -= board[ni][nj] * (10 ** cnt)


T = int(input())

di = [1,-1,0,0]
dj = [0,0,1,-1]

for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    numbers = set()
    for i in range(4):
        for j in range(4):
            tmp = board[i][j]
            cnt = 1
            back(i,j,tmp,cnt)
    print(f'#{tc}',len(numbers))