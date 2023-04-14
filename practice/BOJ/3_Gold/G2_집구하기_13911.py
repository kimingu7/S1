V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

M, x = map(int, input().split())
mcdonalds = list(map(int, input().split()))

S, y = map(int, input().split())
starbucks = list(map(int, input().split()))