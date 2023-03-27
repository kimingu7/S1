t = int(input())

for i in range(t):
    n = int(input())
    box = list(map(int, input().split()))
    max_fall = 0
    for j in range(n):
        cnt = 0
        for k in range(j+1, n):
            if box[j] > box[k]:
                cnt += 1
        if cnt > max_fall:
            max_fall = cnt
    print(f'#{i+1} {max_fall}')