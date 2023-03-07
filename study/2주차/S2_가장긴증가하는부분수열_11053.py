n = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# lst의 i번째 원소가 lst의 j번째 원소보다 클 때 dp[i]는 dp[j] 중 가장 큰 값을 +1 한 값
# 맨처음엔 dp = [0 for _ in range(n)]으로 뒀으나
# dp[0]이 1이라는걸 확인하고 dp = [1 for _ in range(n)]으로 둠