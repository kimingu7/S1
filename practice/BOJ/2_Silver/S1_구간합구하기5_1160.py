import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sum_ = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(sum_)

# dp[1][3] = dp[1][2] + dp[0][3] - dp[0][2] + graph[1][3]
# dp[0][2]는 dp[1][2]와 dp[0][3]에서 중복된 부분