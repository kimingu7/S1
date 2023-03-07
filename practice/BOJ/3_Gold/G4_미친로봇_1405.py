N, e, w, s, n = map(int, input().split())

def back(i,j,visited,total):
    global answer
    if len(visited) == N+1:
        answer += total
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if (ni, nj) not in visited:
            visited.append((ni,nj))
            back(ni,nj,visited,total*percent[k])
            visited.pop()


di = [-1,1,0,0]
dj = [0,0,-1,1]
percent = [e,w,s,n]
answer = 0
back(0,0,[(0,0)],1)
answer = answer * (0.01 ** N)
print(answer)

# 백트래킹을 활용해 이동하지 않은 곳으로만 진행할 확률을 구하는 문제
# 한번 이동할 때마다 total에 방향으로 이동할 확률을 곱해서 계산
# 이동을 끝낼 때마다 answer에 total을 더해서 누적
# 마지막에 진행한 횟수만큼 0.01을 곱해야함