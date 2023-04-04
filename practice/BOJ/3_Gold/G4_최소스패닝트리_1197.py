def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x: x[2])
parent = [i for i in range(v+1)]

answer = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a,b)
        answer += c
print(answer)

# 최소 스패닝 트리 문제를 Kruskal Algorithm을 이용해 구함
# Union-Find를 활용해 구할 수 있음
# edges 배열을 가중치 기준으로 오름차순으로 정렬함
# cost가 작은 edge부터 하나씩 추가하며 같은 부모를 공유하지 않을 때(사이클을 형성하지 않을 때)만 확정