def DFS(start,end):
    stack = []
    visited = [0 for _ in range(101)]
    stack.append(start)
    while stack:
        n = stack.pop()
        visited[n] = 1
        for k in range(101):
            if not visited[k]:
                if graph[n][k]:
                    stack.append(k)
    return visited[end]

for i in range(10):
    t, l = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[0 for _ in range(101)] for _ in range(101)]
    for j in range(0,(l*2)-1,2):
        a, b = lst[j], lst[j+1]
        graph[a][b] = 1
    print(f'#{t} {DFS(0,99)}')

# 그래프경로와 같이 시작점과 끝점의 연결 상태만 확인하는 문제
# DFS를 이용해 끝점의 visited가 1인지만 확인해주면 됨
# 자꾸 끝까지 안가고 중간에서 찍 싸길래 그거에 대한 고민을 했음
# 생각해보니 애초에 그래프를 만들 때 l에 2를 곱해야했었음
# 테스트 케이스의 길이가 l이 아닌 l*2였기 때문
# 문제만 잘읽는게 아니고 테스트 케이스도 잘읽는 착한 코린이가 됩시다