T = int(input())

for tc in range(1,T+1):
    D, M, Q, Y = map(int, input().split())
    plan = list(input().split())
    for i in range(12):
        plan[i] = int(plan[i])
    dp = [0 for _ in range(12)]
    dp[0] = min(D * plan[0], M)
    dp[1] = dp[0] + min(D * plan[1], M)
    dp[2] = min(dp[1] + min(D * plan[2], M), Q)
    for i in range(3, 12):
        dp[i] = min(dp[i-1] + min(D * plan[i], M), dp[i-3] + Q)
    ans = min(dp[11],Y)
    print(f'#{tc}', ans)

# dp를 이용해 간단히 풀 수 있는 문제
# dp[0]은 1월의 방문일 수에 일 요금을 곱한 것과 월 요금 중 최소값
# dp[1]은 2월의 방문일 수에 일 요금을 곱한 것과 월 요금 중 최소값과 dp[0]을 합친 값
# dp[2]는 3월까지의 합과 분기 요금 중 최소값임
# dp[i]는 3달 전까지의 요금의 합에 분기 요금을 더한 값과 i월까지의 합 중 최소값
# 따라서 12월의 요금의 합과 9월까지의 요금의 합에 10 11 12월 요금을 더한 값 중 최소값을 구하면 됨