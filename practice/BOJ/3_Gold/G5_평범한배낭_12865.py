n, k = map(int, input().split())

things = [list(map(int, input().split())) for _ in range(n)]
things.insert(0,[0,0])
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        weight = things[i][0]
        value = things[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])

# knapsack Problem 문제로, 0-1 Knapsack 유형임
# 기존에 있던 조합에서 하나를 빼고, 다른 하나를 넣는 것으로 다음 조합을 만들 수 있고,
# 각 무게마다 최대로 담을 수 있는 2차원 dp 배열을 만들 수 있음
