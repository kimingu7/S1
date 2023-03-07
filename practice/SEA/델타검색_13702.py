for i in range(10):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for j in range(n):
        lst[j] = list(map(int, input().split()))
    sum_xy = 0
    for x in range(n):
        for y in range(n):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    sum_xy += abs(lst[nx][ny] - lst[x][y])
    print(f'#{i+1} {sum_xy}')

# 수업시간에 배운 델타검색을 활용해 리스트의 절댓값 차의 합을 구하면 됨
# if 0 <= nx < n and 0 <= ny < n: 가 중요(IndexError를 방지하기 위해서 사용)