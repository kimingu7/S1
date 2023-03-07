white_paper = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
count = 0
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y,y+10):
            white_paper[j][k] = 1
for j in range(100):
    for k in range(100):
        if white_paper[j][k] == 1:
            count+=1
print(count)