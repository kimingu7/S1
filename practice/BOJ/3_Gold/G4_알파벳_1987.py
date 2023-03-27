r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

check = [0 for _ in range(26)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
max_cnt = 0
def dfs(i,j,cnt):
    global max_cnt
    max_cnt = max(cnt,max_cnt)
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < r and 0 <= nj < c and not check[ord(board[ni][nj])-65]:
            check[ord(board[ni][nj])-65] = 1
            ncnt = cnt + 1
            dfs(ni,nj,ncnt)
            check[ord(board[ni][nj])-65] = 0
    return max_cnt
check[ord(board[0][0])-65] = 1
max_cnt = dfs(0,0,1)
print(max_cnt)

# 알파벳이 중복되지 않아야하므로 크기 26의 배열 check를 통해 확인
# A의 아스키 코드는 65이므로 A를 갔을 때 0번째 index를 방문처리 하기 위해
# ord(board[ni][nj])-65를 index로 하게 됨