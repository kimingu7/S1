t = int(input())
for i in range(t):
    n = int(input())//10
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for j in range(2,n+1):
        dp[j] = dp[j-1] + (dp[j-2]*2)
    print(f'#{i+1} {dp[n]}')

# n =  n-1 + (n-2)*2인 것을 빠르게 찾아야함
# n을 10으로 나눠야함 안나누면 눈물남