for i in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10001
    for j in range(100):
        if ladder[99][j] == 1:
            cnt = 0
            x = j
            y = 99
            while True:
                if x > 0 and ladder[y][x-1] == 1:
                    while x > 0 and ladder[y][x-1] == 1:
                        x -= 1
                        cnt+=1
                    else :
                        y -= 1
                        cnt+=1
                elif x < 99 and ladder[y][x+1] == 1:
                    while x < 99 and ladder[y][x+1] == 1:
                        x += 1
                        cnt+=1
                    else :
                        y -= 1
                        cnt+=1
                else :
                    y -= 1
                    cnt+=1
                if y == 0:
                    break
            if min_cnt > cnt:
                min_cnt = cnt
                min_idx = x
    print(f'#{t} {min_idx}')