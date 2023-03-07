from collections import deque

a, b = map(int, input().split())

def bfs(a):
    q = deque()
    q.append((a,1))
    while q:
        x, cnt = q.popleft()
        if x > b:
            continue
        if x == b:
            return cnt
        q.append((int(str(x)+'1'),cnt+1))
        q.append((x*2, cnt+1))
    return -1
ans = bfs(a)
print(ans)

# bfs를 통해 풀 수 있음
# x가 a에서 b까지 갈 때까지 +1 또는 *2를 진행
# 연산할 때마다 cnt 증가
# b에 도달하면 cnt return
# b에 도달할 수 없으면 -1을 return