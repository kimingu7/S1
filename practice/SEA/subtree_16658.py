T = int(input())

def subtree(n):
    global result
    result+=1
    for i in graph[n]:
        subtree(i)

for tc in range(1,T+1):
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    graph = [[] for _ in range(e+2)]
    index = 1
    for i in tree[::2]:
        graph[i].append(tree[index])
        index+=2
    result = 0
    subtree(n)
    print(f'#{tc}', result)

# 주어진 부모 자식 노드 쌍에서 정점 n의 서브 트리에 속한 노드의 개수를 알아내야함
# 방향성이 있는 graph를 생성한 뒤 연결된 노드를 확인할 때마다 result를 증가