T = int(input())

for tc in range(1,T+1):
    n = int(input())
    number = [0] + list(map(int, input().split()))
    answer = 0
    for i in range(1, n+1):
        while number[i//2] > number[i]:
            number[i//2], number[i] = number[i], number[i//2]
            i//=2
    p = n//2
    while p > 0:
        answer += number[p]
        p//=2
    print(f'#{tc}', answer)

# 마지막 노드의 조상노드들의 누적합을 계산하는 문제
# 1번노드부터 계산해야 편리하기 때문에 number를 [0] + list 과 같이 입력받음
# line 7-10에서 힙 정렬을 진행
# line 12-14에서 answer에 마지막 노드의 조상 노드들의 값을 누적