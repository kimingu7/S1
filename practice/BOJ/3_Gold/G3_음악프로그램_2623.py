from collections import deque

def topology_sort():
    q = deque()
    result = []

    for i in range(1, n+1):
        if indegree[i] ==0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    if len(result) != n:
        print(0)
    else :
        for r in result:
            print(r)

n, m = map(int, input().split())
indegree = [0 for _ in range(n+1)]
graph = [[] for i in range(n+1)]

for _ in range(m):
    singer = list(map(int, input().split()))
    for i in range(1, len(singer) - 1):
        graph[singer[i]].append(singer[i+1])
        indegree[singer[i+1]] += 1

topology_sort()

# 위상정렬을 활용해 푸는 문제
