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

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(v+1)]

    answer = 0
    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
            answer += c
    print(f'#{tc}',answer)