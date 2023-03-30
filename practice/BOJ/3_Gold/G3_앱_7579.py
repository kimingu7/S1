n, m = map(int, input().split())
apps = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(costs)+1)] for _ in range(n+1)]
answer = sum(costs)

for i in range(1,n+1):
    memory = apps[i]
    cost = costs[i]
    for j in range(1,sum(costs)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)
        if dp[i][j] >= m:
            answer = min(answer, j)
if m == 0:
    answer = 0
print(answer)

# 평범한 배낭과 같은 knapsack 문제
# 평범한 배낭과 다른 점은 배열 하나가 아닌 apps와 costs의 두 개의 배열이 주어짐