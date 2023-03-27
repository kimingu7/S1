from collections import deque
n, m = map(int, input().split())
a = [i+1 for i in range(n)]
pops = list(map(int, input().split()))
queue = deque(a)
cnt = 0
for i in pops:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else :
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt+=1
            else :
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt+=1
print(cnt)

# queue에서 i의 index가 queue의 크기의 절반보다 작다면 2번 연산
# queue에서 i의 index가 queue의 크기의 절반보다 크다면 3번 연산