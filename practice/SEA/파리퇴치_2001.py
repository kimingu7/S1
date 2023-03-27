t = int(input())
for i in range(t):
    n, m  = map(int, input().split())
    flies = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        flies[j] = list(map(int, input().split()))
    catch_flies = []
    for x in range(n-m+1):
        for y in range(n-m+1):
            sum_catch_flies = 0
            for z in range(m):
                for w in range(m):
                    sum_catch_flies+=flies[x+z][y+w]
            catch_flies.append(sum_catch_flies)
    print(f'#{i+1} {max(catch_flies)}')

# 행렬 하나 더 만들어서 max값 구해주면 됨