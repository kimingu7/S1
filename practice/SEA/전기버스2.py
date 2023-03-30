def back(k, tmp):
    global answer
    if answer < tmp:
        return
    if k >= n:
        answer = tmp
        return
    cnt = station[k]
    for i in range(cnt, 0, -1):
        back(k+i, tmp+1)


T = int(input())
for tc in range(1, T+1):
    station = list(map(int, input().split()))
    n = station.pop(0)-1
    answer = 99999
    back(0,-1)
    print(f'#{tc}',answer)
