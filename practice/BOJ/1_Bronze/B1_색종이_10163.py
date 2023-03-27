n = int(input())
canvas = [[0 for _ in range(1001)] for _ in range(1001)]
for k in range(1,n+1):
    c, r, w, h = map(int, input().split())
    for i in range(r, r+h):
        for j in range(c, c+w):
            canvas[i][j] = k

for k in range(1,n+1):
    score = 0
    for i in range(1001):
        for j in range(1001):
            if canvas[i][j] == k:
                score += 1
    print(score)