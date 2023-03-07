from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 0
    while queue:
        s = queue.popleft()
        for i in graph[s]:
            if visited[i] == 0:
                visited[i] = visited[s] + 1
                queue.append(i)

for tc in range(1,11):
    l, s = map(int, input().split())
    graph = [[] for _ in range(101)]
    contact = list(map(int, input().split()))
    visited = [0 for _ in range(101)]
    for i in range(0,l,2):
        graph[contact[i]].append(contact[i+1])
    bfs(s)
    max_depth = max(visited)
    max_node = 0
    for i in range(len(graph)):
        if visited[i] == max_depth and max_node < i:
            max_node = i
    print(f'#{tc}', max_node)

# 방향성이 있는 graph의 주어진 시작점에서 깊이가 가장 큰 노드를 찾는 문제
# 시작점 s에서 graph를 따라 연결된 node를 방문할 때 visited 배열에 깊이를 저장
# max_depth(최대 깊이)는 max(visited)와 같음
# line 24-26 같은 깊이를 가지는 노드가 여러 개일 수 있으므로 같은 깊이 중 i값이 가장 큰 값을 max_node
# max_node를 출력