T = int(input())

for tc in range(1,T+1):
    n, m, l = map(int, input().split())
    node = [0 for _ in range(n+1)]
    min_idx = n
    for _ in range(m):
        idx, num = map(int, input().split())
        node[idx] = num
        if idx < min_idx:
            min_idx = idx
    for i in range(min_idx-1,0,-1):
        try :
            node[i] = node[i*2] + node[i*2+1]
        except IndexError:
            node[i] = node[i*2]
    print(f'#{tc}', node[l])

# 주어진 자식 노드들에서 부모노드의 값을 구하는 문제
# i번째 노드의 자식 노드는 i*2번째 노드와 i*2+1번째 노드
# 따라서 i번째 노드는 위 두 노드의 합과 같음
# 이 때 자식 노드가 하나인 경우를 고려해 try except 구문으로 실행