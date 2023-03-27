T = int(input())
for tc in range(1,T+1):
    n = int(input())
    town = [list(map(int, input().split())) for _ in range(n+1)]
    house = [] # 집의 위치를 담을 빈 배열 house 선언
    for i in range(n+1):
        for j in range(n+1):
            if town[i][j] == 1:
                house.append((i,j)) # 1일 경우 house에 i,j append
            if town[i][j] == 2: 
                ci,cj = i,j # 2일 경우 중계기의 좌표 ci cj 저장
    max_dist = 0
    while house:
        hi, hj = house.pop()
        dist_s = ((ci-hi)**2+(cj-hj)**2) # 중계기와 집의 거리의 제곱 dist_s
        dist_i = int(dist_s**(1/2))
        dist_f = dist_s**(1/2)
        if dist_i != dist_f:
            dist = int(dist_f)+1
        else :
            dist = dist_i
        if max_dist < dist:
            max_dist = dist
    print(f'#{tc}', max_dist)

# 반지름 R은 중계기로부터 가장 멀리있는 집의 거리와 같을 때 최소임
# 맵 데이터는 (n+1)*(n+1)의 크기임을 유의
# house 배열이 빌 때까지 while 문 진행(모든 집에 대해서 check)
# 중계기의 거리의 제곱근을 구했을 때
# 정수일 경우 그대로 구함
# 정수가 아닐 경우 정수로 바꿔준 뒤 1을 더함