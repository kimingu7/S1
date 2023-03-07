T = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
def moving_rooms(i,j,cnt):
    global max_count
    stack = [(i,j,cnt)]
    while stack:
        ki, kj , cnt = stack.pop()
        for k in range(4):
            ni, nj = ki + di[k], kj + dj[k]
            if 0 <= ni < n and 0 <= nj < n and rooms[ki][kj] + 1 == rooms[ni][nj]:
                stack.append((ni,nj,cnt+1))
                break
    if max_count <= cnt:
        max_count = cnt
        countlist.append((rooms[i][j], cnt))


for tc in range(1,T+1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    max_count = 0
    min_room = 10**9
    countlist = []
    for i in range(n):
        for j in range(n):
            moving_rooms(i,j,1)
    for i in range(len(countlist)):
        if countlist[i][1] == max_count:
            if min_room > countlist[i][0]:
                min_room = countlist[i][0]
    print(f'#{tc}', min_room, max_count)

# stack에 저장
# 델타 탐색을 통해 직전 칸보다 1 큰 칸으로만 이동하고, 그 때 count 증가