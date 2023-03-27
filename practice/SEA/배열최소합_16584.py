def back(idx, sum_lst):
    global ans
    if idx == n:
        if ans > sum_lst:
            ans = sum_lst
            return
    if ans < sum_lst:
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            back(idx+1, sum_lst+lst[idx][i])
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    ans = 100
    visited = [0 for _ in range(n)]
    back(0, 0)
    print(f'#{tc} {ans}')

# n*n 배열에서 행마다 서로 다른 열을 골라 최소합을 구하는 문제
# n이 최대 10이고 10보다 작은 자연수가 주어지기에 최대값을 100으로 둠
# line 3 idx가 n번째행에 도달했을 때
# line 4 ans가 sum_lst보다 작다면 ans = sum_lst
# line 7 만약 sum_lst가 ans보다 커진다면 즉시 return
# line 9 중복되는 열을 고르지 않기 위해 sum_lst에 lst[idx][i]가 더해질 때마다 visited[i]도 1로 둠

# line 7-8에서 sum_lst가 ans보다 커질 때 즉시 return을 해야함
# 그렇지 않으면 모든 경우의 수를 탐색하기 때문에 시간초과가 발생