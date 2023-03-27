def DFS(start, end):
    stack = []
    visited = [0 for _ in range(v+1)]
    stack.append(start)
    while stack:
        n = stack.pop()
        visited[n] = 1
        for k in range(1,v+1):
            if not visited[k]:
                if graph[n][k]:
                    stack.append(k)
    return visited[end]

t = int(input())
for i in range(t):
    v, e = map(int, input().split())
    graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
    for j in range(e):
        start, end = map(int, input().split())
        graph[start][end] = 1
    s, g = map(int, input().split())
    print(f'#{i+1} {DFS(s,g)}')

# DFS를 활용해서 푸는 문제
# line 6에서 스택에 둔 start를 pop해서 n으로 할당
# visited할 경우 1, 아닐 경우 0
# line 8 1부터 v+1까지 보면서
# line 9 방문하지 않았고,
# line 10 연결되어있다면
# line 11 stack에 k를 append
# line 12 end에 들렀는지 return (들렀다면 1, 아니라면 0)
# line 21-22 DFS(s,g)에서 return 된 값을 출력