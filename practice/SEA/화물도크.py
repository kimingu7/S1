T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cargo = [list(map(int, input().split())) for _ in range(n)]
    cargo.sort(key=lambda x : (x[1], x[0]))
    count = 1
    dock = cargo[0]
    for i in range(1,n):
        if cargo[i][0] >= dock[1]:
            dock = cargo[i]
            count+=1
    print(f'#{tc}',count)

# 도크를 x[1] 기준으로 정렬
# 맨처음 도크를 실어줌
# 이 때 화물의 시작 시간이 도크에 실린 화물의 도착 시간 이상일 때
# 도크를 교체하고, count 1 증가
# count 출력