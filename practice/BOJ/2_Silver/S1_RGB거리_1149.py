n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
for i in range(1,n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])
print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))

# dp 문제인줄 모르고 풀다보니 경우의 수가 길어졌는데 마지막을 보니 dp인걸 깨달음
# 이전의 것과 다른 index의 값 중 가장 작은 값을 누적해서 더해나가면 됨
# 따라서 [i][0], [i][1], [i][2]로 시작하는 모든 경우의 수를 만들어 체크