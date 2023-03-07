from collections import deque

def bfs(i,j,color):
    q = deque()
    q.append((i,j))
    pang = deque()
    pang.append((i,j))
    visited = [[0 for _ in range(6)] for _ in range(12)]
    visited[i][j] = 1
    count = 1
    flag = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni > 11 or nj < 0 or nj > 5:
                continue
            if puyopuyo[ni][nj] == color and not visited[ni][nj]:
                q.append((ni,nj))
                pang.append((ni,nj))
                visited[ni][nj] = 1
                count+=1
    if count >= 4:
        flag = 1
        for a, b in pang:
            puyopuyo[a][b] = '.'
    return flag


def falling():
    for j in range(6):
        q = deque()
        for i in range(11,-1,-1):
            if puyopuyo[i][j] != '.':
                q.append(puyopuyo[i][j])
        for i in range(11,-1,-1):
            if q:
                puyopuyo[i][j] = q.popleft()
            else :
                puyopuyo[i][j] = '.'


puyopuyo = [list(input()) for _ in range(12)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
chain = 0
while True:
    check = 0
    for i in range(12):
        for j in range(6):
            if puyopuyo[i][j] != '.':
                check += bfs(i,j,puyopuyo[i][j])
    if check == 0:
        print(chain)
        break
    else :
        chain+=1
    falling()

# line 3-28 bfs를 돌리면서 뿌요뿌요를 터트림 (폭*팔)
# line 31-41 떨어지는 뿌요뿌요를 다시 정렬