T = int(input())

for tc in range(1,T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    profit = 0
    r = c = n//2
    for i in range(n):
        for j in range(n):
            if abs(r-i) + abs(c-j) <= n//2:
                profit += farm[i][j]
    print(f'#{tc}',profit)

# 중심점에서 맨해튼 거리가 n//2 이하인 칸들의 합을 출력하는 문제