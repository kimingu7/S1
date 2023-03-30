def back(k, tmp):
    global answer
    if tmp < answer:
        return
    if k == n:
        if answer < tmp:
            answer = tmp
        return
    for i in range(n):
        if not visited[i] and percent[k][i]:
            tmp = tmp * (percent[k][i] * 0.01)
            visited[i] = 1
            back(k+1, tmp)
            visited[i] = 0
            tmp = tmp / (percent[k][i] * 0.01)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    percent = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    answer = 0
    back(0,1)
    answer = answer * 100
    print(f'#{tc} {answer:.6f}')
    
# backtracking을 활용해 최대값을 구하는 문제
# 시간초과가 뜨지 않게 하기 위해 percent[k][i]가 0이 아닐 때를 제외
# 이 때 answer를 7자리에서 반올림 하기 위해 round를 썼으나 .000000과 같은 케이스를 .0으로 출력해 오답이 됨
# f string을 활용해 해결할 수 있었음