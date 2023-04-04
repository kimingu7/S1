def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    list_m = list(map(int, input().split()))
    parent = [i for i in range(n+1)]
    for i in range(0,len(list_m),2):
        union(list_m[i], list_m[i+1])
    result = set()
    for i in range(1,n+1):
        result.add(find(i))
    answer = len(result)
    print(f'#{tc}',answer)
    
# union-find를 활용해 푸는 문제
# 경로 최적화를 위해 find 함수의 return 값을 x가 아닌 parent[x]
# 이 때 주어진 리스트에서 list_m[i], list_m[i+1]에 대해 union 함수 실행
# 부모 노드의 리스트 result는 set으로 둠
# reuslt에 모든 노드의 부모노드를 find 함수를 통해 저장 (find 함수의 return 값이 parent[x]기 때문)
# answer는 len(result)