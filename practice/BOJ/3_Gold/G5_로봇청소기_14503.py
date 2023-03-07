n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

count = 0
while True:
    if room[r][c] == 0:
        room[r][c] = -1
        count+=1
    cnt = 0
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if room[nr][nc] != 0:
            cnt+=1
    if cnt == 4:
        if d < 2:
            d+=2
        else :
            d-=2
        if room[r+dr[d]][c+dc[d]] == 1:
            break
        else :
            r = r + dr[d]
            c = c + dc[d]
            if d < 2:
                d+=2
            else :
                d-=2
    else :
        if d == 0:
            d = 3
        else :
            d-=1
        if room[r+dr[d]][c+dc[d]] == 0:
            r = r+dr[d]
            c = c+dc[d]
print(count)

# 현재 위치한 칸이 0이면 -1로 바꾸고 cnt 증가
# 델타탐색을 통해 주변 4칸 중 청소가 되지 않은 칸 탐색
# 청소가 되지 않은 칸이 없다면 후진할 수 있는지 확인 후 없으면 break
# 후진할 수 있다면 후진
# 청소가 되지 않은 칸이 있다면 반시계방향으로 돌린 후 청소가 되지 않은 칸일 때 전진