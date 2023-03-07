from collections import deque

def BFS(x):
    global cnt
    queue = deque([x])
    cnt = 0
    while queue:
        x = queue.popleft()
        if x == k:
            cnt+=1
            continue
        for m in (x-1, x+1, x*2):
            if 0 <= m < end and (not lst[m] or lst[m] == lst[x] + 1):
                lst[m] = lst[x] + 1
                queue.append(m)
n, k = map(int, input().split())
end = 100001
lst = [0 for _ in range(end)]
BFS(n)
print(lst[k])
print(cnt)

# 숨바꼭질 시리즈의 두번째 문제
# line 11 x가 k일 때 cnt 값만 증가시키고 continue를 해줘야함 (여러 번 찾기 위해)
# line 13 lst[m]이 없거나 lst[m]이 lst[x]+1일 때만 더 함