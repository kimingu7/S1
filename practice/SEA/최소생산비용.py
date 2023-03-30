def back(k):
    global answer, tmp
    if answer <= tmp:
        return
    if k == n:
        if answer > tmp:
            answer = tmp
        return
    for i in range(n):
        if not visited[i]:
            tmp += factory[k][i]
            visited[i] = 1
            back(k+1)
            visited[i] = 0
            tmp -= factory[k][i]

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    factory = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    answer = 99999
    tmp = 0
    back(0)
    print(f'#{tc}',answer)

# backtracking을 활용해 최소값을 구하는 문제
# 중간에 tmp 값이 answer보다 커지는 경우에 return
# k가 n (끝까지 도달했을 때) tmp 값이 answer보다 작을 때 answer에 tmp 할당