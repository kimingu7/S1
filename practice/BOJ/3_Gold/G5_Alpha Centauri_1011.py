t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    d = y - x
    cnt = 0
    move = 1
    sum_move = 0
    while sum_move < d :
        cnt+=1
        sum_move += move
        if cnt%2 == 0:
            move+=1
    print(cnt)