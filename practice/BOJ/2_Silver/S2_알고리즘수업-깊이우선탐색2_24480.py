import sys
sys.setrecursionlimit(10**9)
def DFS(s):
    global count
    visited[s] = count
    graph[s].sort(reverse=True)
    for i in graph[s]:
        if not visited[i]:
            count+=1
            DFS(i)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
count = 1

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(r)

for i in range(1, n+1):
    print(visited[i])

# n개의 정점을 m개의 간선으로 연결했을 때 
# 정점 r에서 DFS를 실행해 방문하는 정점을 순서대로 출력하는 문제
# 순서대로 출력하기 위해 DFS에서 graph[s].sort()를 실행해줌
# 이 때 1과는 달리 내림차순으로 출력하기 때문에 reverse=True를 추가
# 방문할 때마다 visited 배열에 count 값만큼 추가해줌
# r에서 n번째 정점에 방문할 경우 visited[n]에 n을 더해주고, 방문하지 않는다면 visited[n]은 그대로 0
# 1 2 3 4 순으로 방문하고, 5번은 방문하지 않음

# 해당 문제에서 RecursionError가 발생했음
# 백준의 가이드 라인에 따라 sys.setrecursionlimit를 사용해 10^9로 제한했음
# 그러나 Python3에선 시간 초과가, PyPy3에선 메모리 초과가 발생함
# Python3에서 input을 sys.stdin.readline로 대체하여 해결함