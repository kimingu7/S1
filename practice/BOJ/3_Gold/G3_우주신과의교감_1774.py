import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
gods = [0]
edges = []
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    gods.append((x,y))
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
for i in range(1,n):
    for j in range(i+1,n+1):
        edge = math.sqrt((gods[i][0]-gods[j][0])**2+(gods[i][1]-gods[j][1])**2)
        edges.append((i,j,edge))
edges.sort(key = lambda x:x[2])

for i in edges:
    a, b, edge = i
    if find(a) != find(b):
        union(a, b)
        answer+=edge
print(f'{answer:.2f}')

# kruskal 알고리즘을 활용해 길이의 합을 최소로 만들도록 함
# 신들의 위치인 gods 배열에 위치를 저장
# 이미 주어진 m개의 배열들을 먼저 union-find를 통해 연결
# edges 배열에 i, j와 i, j 사이의 거리 edge를 저장
# 거리 기준으로 정하고 kruskal 알고리즘을 통해 최소 스패닝 트리를 구함