import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(start_node):
    global cnt
    cnt+=1
    queue = deque([])
    queue.append((start_node[0], start_node[1]))
    while queue:
        x,y = queue.pop()
        field[x][y] = 0
        for k in range(4):
            if 0 <= x+dx[k] < n and 0 <= y+dy[k] < m:
                if field[x+dx[k]][y+dy[k]] == 1:
                    queue.append((x+dx[k], y+dy[k]))

for i in range(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for j in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1
    for x in range(n):
        for y in range(m):
            if field[x][y] == 1:
                BFS((x,y))
    print(cnt)