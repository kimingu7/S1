from collections import deque

def BFS(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if x == k:
            return lst[x]
        for m in (x-1, x+1, x*2):
            if 0 <= m < end and not lst[m]:
                lst[m] = lst[x] + 1
                queue.append(m)
n, k = map(int, input().split())
end = 100001
lst = [0 for _ in range(end)]
print(BFS(n))

# BFS를 활용해서 푸는 숨바꼭질 문제
# BFS는 deque를 활용해서 푼다
# x가 k에 도달할 때까지 BFS를 계속 진행함
# line 9 m은 x-1, x+1, x*2 중 하나로 이동함
# line 10 m이 0과 end 사이에서만 움직이도록 하고, lst[m]이 없을 때만 1 증가
# line 11 lst[m]은 lst[x] + 1 (깊이)