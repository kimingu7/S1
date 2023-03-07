t = int(input())
for i in range(t):
    canvas = [[0 for _ in range(10)] for _ in range(10)]
    count = 0
    n = int(input())
    lst = [[0 for _ in range(5)] for _ in range(n)]
    for j in range(n):
        lst[j] = list(map(int, input().split()))
    for j in range(n):
        r1, r2, c1, c2, color = lst[j][0], lst[j][1], lst[j][2], lst[j][3], lst[j][4]
        for x in range(10):
            for y in range(10):
                if color == 1 and r1 <= x <= c1 and r2 <= y <= c2 and lst != 1:
                    canvas[x][y]+=1
                elif color == 2 and r1 <= x <= c1 and r2 <= y <= c2 and lst != 2:
                    canvas[x][y]+=2
    for x in range(10):
        for y in range(10):
            if canvas[x][y] == 3:
                count+=1
    print(f'#{i+1} {count}')

# 같은 색끼리 영역이 겹치지 않는다는 조건이 있는걸 모르고 겹쳤을 때를 상정한 조건을 추가했음
# 없어도 무관
# 빨강색 영역은 1 파랑색 영역은 2를 더해 3이 되는 영역을 카운트