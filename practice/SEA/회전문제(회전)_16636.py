T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    i = m%n
    print(f'#{tc}', queue[i])

# 야매로 푼 문제