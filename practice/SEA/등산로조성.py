def dfs(i,j,cnt):
    global answer
    if answer < cnt:
        answer = cnt
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < n and 0 <= nj < n:
            if maps[ni][nj] < maps[i][j]:
               dfs(ni,nj,cnt+1)

di = [1,-1,0,0]
dj = [0,0,1,-1]
T = int(input())
for tc in range(1,T+1):
    n, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    max_value = max(map(max, maps))
    peirece = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == max_value:
                peirece.append((i,j))
    for i in range(n):
        for j in range(n):
            for k in range(K):
                maps[i][j] -= k+1
                for l in range(len(peirece)):
                    r = peirece[l][0]
                    c = peirece[l][1]
                    if maps[r][c] == max_value:
                        dfs(r,c,1)
                maps[i][j] += k+1
    print(f'#{tc}',answer)