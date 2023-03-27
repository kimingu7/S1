r, c, t = map(int, input().split())

di = [1,-1,0,0]
dj = [0,0,1,-1]

room = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            r2 = i
            c1 = j
r1 = r2 - 1
sec = 0
while sec < t:
    n_room = [[0 for _ in range(c)] for _ in range(r)]
    n_room[r1][c1] = n_room[r2][c1] = -1
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                move_count = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < r and 0 <= nj < c:
                        if room[ni][nj] != -1:
                            n_room[ni][nj] += int(room[i][j]/5)
                            move_count += 1
                n_room[i][j] += room[i][j] - int(room[i][j]/5) * move_count
    room = [[0 for _ in range(c)] for _ in range(r)]
    room[r1][c1] = room[r2][c1] = -1
    for j in range(1,c-1):
        room[r1][j+1] = n_room[r1][j]
        room[r2][j+1] = n_room[r2][j]
    for i in range(r1-1,-1,-1):
        room[i][c-1] = n_room[i+1][c-1]
    for i in range(r2+1,r):
        room[i][c-1] = n_room[i-1][c-1]
    for j in range(c-2,-1,-1):
        room[0][j] = n_room[0][j+1]
        room[r-1][j] = n_room[r-1][j+1]
    for j in range(1,r1):
        if room[j][0] != -1:
            room[j][0] = n_room[j-1][0]
    for j in range(r-2,r2,-1):
        if room[j][0] != -1:
            room[j][0] = n_room[j+1][0]
    for i in range(1,r1):
        for j in range(1,c-1):
            room[i][j] = n_room[i][j]
    for i in range(r2+1,r-1):
        for j in range(1,c-1):
            room[i][j] = n_room[i][j]
    sec+=1

dust = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            dust += room[i][j]

print(dust)

# 반드시 확산을 먼저 시킨 뒤 공기청정기로 순환을 시켜야함
# 확산은 델타 검색을 응용하면 됨
# 확산된 방 n_room과 n_room에서 이동시킬 방 room을 매 초마다 초기화 후 재할당하는 방식으로 진행