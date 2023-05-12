n = int(input())
INF = int(1e9)
answer = INF
cost = [list(map(int, input().split())) for _ in range(n)]
for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = cost[0][i]
    for j in range(1,n):
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])
    for j in range(3):
        if i != j:
            answer = min(answer, dp[n-1][j])

print(answer)