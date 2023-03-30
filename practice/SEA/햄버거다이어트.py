T = int(input())

for tc in range(1,T+1):
    n, l = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(n)]
    ingredients.insert(0,[0,0])
    dp = [[0 for _ in range(l+1)] for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, l+1):
            taste = ingredients[i][0]
            calories = ingredients[i][1]
            if j < calories:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-calories] + taste)
    print(f'#{tc}',dp[n][l])
    
# knapsack 알고리즘 문제