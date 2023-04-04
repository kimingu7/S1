import heapq

def djikstra(s):
    q = []
    heapq.heappush(q, (0,s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

T = int(input())
INF = 1e9
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e,w))
    distance = [INF for _ in range(N+1)]
    djikstra(0)
    print(f'#{tc}',distance[N])
    
# djikstra 기초적인 문제
# heapq를 사용해 구현함