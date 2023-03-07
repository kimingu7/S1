from collections import deque

def DFS(graph, root):
    lst = []
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in lst:
            lst.append(n)
            if n in graph:
                tmp = list((set(graph[n])) - set(lst))
                tmp.sort(reverse=True)
                stack+=tmp
    return " ".join(str(i) for i in lst)

# DFS에선 BFS와 달리 stack 자료 구조를 사용함 (한 방향으로 쭉 탐색하기 위해)

def BFS(graph, root):
    lst = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in lst:
            lst.append(n)
            if n in graph:
                tmp = list((set(graph[n])) - set(lst))
                tmp.sort()
                queue+=tmp
    return " ".join(str(i) for i in lst)

# BFS의 핵심은 queue 자료 구조를 사용하는 것(deque를 사용해 시간을 절약하자)
# 방문하지 않은 노드를 queue에 넣을 때 set을 사용해 쉽게 구현


graph = {}
n, m, v = map(int, input().split())
for i in range(m):
    n1, n2 = map(int,input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
print(DFS(graph, v))
print(BFS(graph, v))

# 제시된 예제에서 1 2, 1 3, 1 4, 2 4, 3 4가 연결됨을 확인
# 그래프를 만들 때 주의
# DFS의 경우 1 2를 먼저 탐색하고, 2 4가 연결되있기에 4까지 탐색 후 돌아와 3을 탐색
# BFS의 경우 1 2를 탐색하고 다시 3을 탐색한 뒤 4까지 탐색