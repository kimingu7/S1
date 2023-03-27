t = int(input())
for i in range(t):
    k, n, m = map(int, input().split())
    station = list(map(int, input().split()))
    station.append(n)
    cnt = 0
    bus = 0
    fuel = k
    while bus <= n:
        for a in range(m):
            if bus == station[a]:
                if bus + fuel >= station[a + 1]:
                    pass
                else:
                    fuel = k
                    cnt += 1
        if fuel <= 0 and bus != n:
            cnt = 0
            break
        fuel -= 1
        bus += 1
    print(f'#{i + 1} {cnt}')

# bus가 1칸씩 전진할 때마다 fuel이 1씩 감소
# bus가 station에 도착했을 때 다음 station까지 갈 fuel이 충분하다면 pass
# 충분하지 않다면 fuel=k, cnt+=1 해줌
# fuel이 0인데 도착지가 아니라면 cnt=0으로 주고 정지시킴