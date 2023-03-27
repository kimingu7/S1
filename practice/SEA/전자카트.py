def back(count, x, sum_battery):
    global answer
    if count == n:
        sum_battery += golf[x][0]
        if answer > sum_battery:
            answer = sum_battery
            return
    if answer < sum_battery:
        return
    for i in range(1,n):
        if not golf[x][i]:
            continue
        if not visited[i]:
            visited[i] = 1
            back(count+1, i, sum_battery + golf[x][i])
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    golf = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    answer = n * 100
    back(1,0,0)
    print(f'#{tc}', answer)