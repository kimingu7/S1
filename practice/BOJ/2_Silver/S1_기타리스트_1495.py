n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j] != 0:
            if j + v[i-1] >= 0 and j + v[i-1] <= m:
                dp[i][j+v[i-1]] = 1
            if j - v[i-1] >= 0 and j - v[i-1] <= m:
                dp[i][j-v[i-1]] = 1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        p = i
        break
    else :
        p = -1
print(p)