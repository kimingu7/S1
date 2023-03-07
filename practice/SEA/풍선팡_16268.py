t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    ballon = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    max_ballon = 0
    for x in range(n):
        for y in range(m):
            sum_flower = ballon[x][y]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    sum_flower += ballon[nx][ny]
            if max_ballon < sum_flower:
                max_ballon = sum_flower
    print(f'#{i+1} {max_ballon}')