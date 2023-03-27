T = int(input())

di1 = [1,-1,0,0]
dj1 = [0,0,1,-1]
di2 = [1,1,-1,-1]
dj2 = [1,-1,1,-1]

def spray1(i,j):
    catch1 = area[i][j]
    for l in range(1,m):
        for k in range(4):
            ni = i + (di1[k] * l)
            nj = j + (dj1[k] * l)
            if 0 <= ni < n and 0 <= nj < n:
                catch1 += area[ni][nj]
    return catch1

def spray2(i,j):
    catch2 = area[i][j]
    for l in range(1,m):
        for k in range(4):
            ni = i + (di2[k] * l)
            nj = j + (dj2[k] * l)
            if 0 <= ni < n and 0 <= nj < n:
                catch2 += area[ni][nj]
    return catch2

for tc in range(1, T+1):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    max_catch = 0
    for i in range(n):
        for j in range(n):
            catch1 = spray1(i,j)
            catch2 = spray2(i,j)
            max_catch = max(catch1, catch2, max_catch)
    print(f'#{tc}', max_catch)

# 델타탐색을 응용