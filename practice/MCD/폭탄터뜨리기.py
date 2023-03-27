def boom(i,j):
    for a in range(4):
        for b in range(1,k+1):
            ni = i + b*di[a]
            nj = j + b*dj[a]
            if 0 <= ni < n and 0 <= nj < m:
                if site[ni][nj] == '#':
                    break
                elif site[ni][nj] == '_':
                    site[ni][nj] = '%'

n, m = map(int, input().split())
k = int(input())
site = [list(input()) for _ in range(n)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
for i in range(n):
    for j in range(m):
        if site[i][j] == '@':
            site[i][j] = '%'
            boom(i,j)

for i in site:
    print(*i,sep='')