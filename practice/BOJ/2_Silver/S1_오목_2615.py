board = [list(map(int, input().split())) for _ in range(19)]

di = [1,1,0,-1]
dj = [0,1,1,1]
winner = 0

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            start = board[i][j]
            for k in range(4):
                count = 1
                ni = i + di[k]
                nj = j + dj[k]
                while 0 <= ni < 19 and 0 <= nj < 19 and board[ni][nj] == start:
                    count+=1
                    if count == 5:
                        if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19 and board[i - di[k]][j - dj[k]] == start:
                            break
                        if 0 <= ni + di[k] < 19 and 0 <= nj + dj[k] < 19 and board[ni + di[k]][nj + dj[k]] == start:
                            break
                        winner = start
                        print(winner)
                        print(i+1,j+1)
                        exit()
                    ni += di[k]
                    nj += dj[k]
print(winner)