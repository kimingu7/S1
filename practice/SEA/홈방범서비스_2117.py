T = int(input())

def security_cost(k):
    return k*k + (k-1)*(k-1)

def security_service(k):
    global cost, house, max_house
    cost = house = 0
    for i in range(n):
        for j in range(n):
            cost = house = 0
            for a in range(n):
                for b in range(n):
                    if abs(i-a) + abs(j-b) < k:
                        if city[a][b] == 1:
                            cost+=m
                            house+=1
            cost = cost - security_cost(k)
            if cost >= 0 and max_house < house:
                max_house = house


for tc in range(1, T+1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    max_house = 0
    for k in range(1,n+2):
        security_service(k)
    print(f'#{tc}', max_house)

# 코드에는 문제가 없었다. 문제는 나에게 있었을 뿐
# 기준점에서 거리가 k 미만인 점 중에 집일 때마다 house를 1씩, cost를 m씩 증가
# 이 때 cost가 0 이상일 때 house가 가장 큰 값을 저장