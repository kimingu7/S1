from collections import deque

def bfs(n,m):
    queue = deque()
    queue.append((n,0))
    visited = {}
    while queue:
        n, count = queue.popleft()
        count+=1
        if visited.get(n,0):
            continue
        visited[n] = 1
        if n == m:
            count-=1
            return count
        if 0 < n+1 <= 1000000:
            queue.append((n+1,count))
        if 0 < n-1 <= 1000000:
            queue.append((n-1,count))
        if 0 < n*2 <= 1000000:
            queue.append((n*2,count))
        if 0 < n-10 <= 1000000:
            queue.append((n-10,count))

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    answer = bfs(n,m)
    print(f'#{tc}',answer)

# bfs를 통해 푸는 문제
# boj의 숨바꼭질 문제와도 유사(end가 1000000인 부분을 제외하면 유사)
# 이미 연산과정에서 나온 숫자가 또 나오는 경우를 방지하기 위해 visited라는 dictionary 정의
# 연산 중간에도 값이 1000000을 넘지 않도록 체크하며 4가지 경우에 대해 bfs 진행