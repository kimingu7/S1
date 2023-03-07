T = int(input())

def taste():
    global min_taste
    taste = 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                taste += synergy[i][j]
            elif not visited[i] and not visited[j]:
                taste -= synergy[i][j]
    min_taste = min(min_taste, abs(taste))
    return

def cook(ing, num):
    if num > n // 2:
        return
    if ing == n-1:
        if num == n//2:
            taste()
        return

    cook(ing+1,num)
    visited[ing] = 1

    cook(ing+1,num+1)
    visited[ing] = 0

for tc in range(1, T+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_taste = 1000000
    cook(0,0)
    print(f'#{tc}',min_taste)

# 재료를 두 그룹으로 나누는 cook 함수
# 한 그룹의 재료 수는 n//2이며 visited 하지 않은 재료를 추가
# 재료 n개는 n//2개의 visited인 재료와 not visited인 재료로 나뉨
# 나눠진 재료들의 맛의 차를 구하는 taste 함수
# taste는 visited인 재료들의 시너지의 합들에서 not visited인 재료들의 시너지들의 합을 빼준 것과 같음
# 이 때 모든 재료를 나누는 경우에서 min_taste 값을 구해줌
