from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs():
    global answer
    q = deque([(0,0)])
    visited = [[0 for _ in range(w+2)] for _ in range(h+2)]
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h+2 and 0 <= nj < w+2 and not visited[ni][nj]:
                if building[ni][nj] == '*':
                    continue
                if ord('A') <= ord(building[ni][nj]) <= ord('Z'):
                    continue
                if building[ni][nj] == '$':
                    answer+=1
                if ord('a') <= ord(building[ni][nj]) <= ord('z'):
                    keys.append(building[ni][nj])
                q.append((ni,nj))
                building[ni][nj] = '.'
                visited[ni][nj] = 1


T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    building = [['.' for _ in range(w+2)]]
    for _ in range(h):
        row = input()
        row = '.' + row + '.'
        building.append(list(''.join(row)))
    building.append(['.' for _ in range(w+2)])
    keys = list(input())
    answer = 0
    while keys:
        if keys[0] == '0':
            keys.clear()
        if keys:
            for i in range(h+2):
                for j in range(w+2):
                    if building[i][j].lower() in keys:
                        building[i][j] = '.'
            keys.clear()
        bfs()
    print(answer)