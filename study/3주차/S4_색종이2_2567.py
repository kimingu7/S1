n = int(input())
canvas = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            canvas[i][j] = 1
di = [1,-1,0,0]
dj = [0,0,1,-1]
length = 0
for i in range(101):
    for j in range(101):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 101 and 0 <= nj < 101:
                if canvas[i][j] == 1 and canvas[ni][nj] != 1:
                    length+=1
print(length)

# 델타탐색을 했을 때 주변에 0이 없는 1이라면 테두리임
# 테두리에 있는 모든 1을 세면 그것이 둘레의 길이