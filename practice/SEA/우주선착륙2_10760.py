di = [1,1,1,0,0,-1,-1,-1]
dj = [1,0,-1,1,-1,1,0,-1]

t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    mars = [list(map(int, input().split())) for _ in range(n)]
    candidate = 0
    for i in range(n):
        for j in range(m):
            center = mars[i][j]
            cnt = 0
            for k in range(8):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < m and center > mars[ni][nj]:
                    cnt += 1
            if cnt >= 4:
                candidate += 1
    print(f'#{tc} {candidate}')

# 쉬운 8방향 델타검색 문제