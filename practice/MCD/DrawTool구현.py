n = int(input())
q = int(input())
canvas = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(q):
    color, y1, x1, y2, x2 = map(int, input().split())
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            if canvas[i][j] < color:
                canvas[i][j] = color
max_square = 0