def back(i):
    global tower, tmp
    if tmp >= b:
        tower.append(tmp)
        return
    for j in range(i+1,n):
        if not visited[j]:
            tmp += heights[j]
            back(j)
            tmp -= heights[j]

T = int(input())

for tc in range(1,T+1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    visited = [0 for _ in range(n)]
    tower = []
    for i in range(n):
        tmp = heights[i]
        back(i)
    answer = min(tower) - b
    print(f'#{tc}', answer)