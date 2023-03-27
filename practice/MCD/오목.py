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

# 델타 탐색을 응용하여 푸는 문제 (오셀로와도 유사함)
# 대각선 위 아래, 아래, 오른쪽 방향으로 확인하면 됨
# 이 때 육목이 되는지 체크하기 위해 앞뒤로 한칸씩을 확인해줌
# 승부가 나지 않는 경우는 for문이 끝난 뒤 0 출력