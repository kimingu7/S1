T = int(input())

for tc in range(1,T+1):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    weights = 0
    for i in range(m):
        for j in range(n):
            if containers[j] <= trucks[i]:
                weights += containers[j]
                trucks[i] = 0
                containers[j] = 100
    print(f'#{tc}', weights)

# 컨테이너와 트럭을 내림차순으로 정렬
# truck의 수용량보다 컨테이너의 무게가 작을 때, weights에 container의 무게 추가
# 이 때 트럭에 실은 컨테이너는 무게를 실을 수 없도록 설정
# weights를 출력