from itertools import combinations

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]
house = []
chickens = []
result = 250000
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        if city[i][j] == 2:
            chickens.append((i,j))
for chicken in combinations(chickens, m):
    temp = 0
    for h in house:
        dist = 1000
        for i in range(m):
            dist = min(dist, abs(h[0] - chicken[i][0]) + abs(h[1] - chicken[i][1]))
        temp += dist
    result = min(result, temp)

print(result)

# itertools의 combinations를 이용해 푸는 문제
# 선택된 m개의 치킨집에서 모든 집까지의 거리 중 가장 작은 값들의 합이 가장 작은 값을 구함