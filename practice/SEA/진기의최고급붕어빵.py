T = int(input())
 
for tc in range(1,T+1):
    n, m, k = map(int, input().split())
    waiting = list(map(int, input().split()))
    waiting.sort()
    result = 'Possible'
    for i in range(n):
        bread = (waiting[i]//m)*k - i
        if bread < 1:
            result = 'Impossible'
            break
    print(f'#{tc}',result)

# 방문할 때 빵의 개수가 1보다 작으면 impossible을 출력하도록 함