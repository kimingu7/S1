n = int(input())
canvas = [[11 for _ in range(6)] for _ in range(6)]
for _ in range(n):
    idx, dir = input().split()
    idx = int(idx)
    for i in range(6):
        if dir == 'L':
            if idx > 0:
                if canvas[5-i][idx] > i+1:
                    canvas[5-i][idx] = i+1
                idx-=1
            elif idx == 0:
                if canvas[5-i][idx] > i+1:
                    canvas[5-i][idx] = i+1
                dir = 'R'
                idx+=1
        elif dir == 'R':
            if idx < 5:
                if canvas[5-i][idx] > i+1:
                    canvas[5-i][idx] = i+1
                idx+=1
            elif idx == 5:
                if canvas[5-i][idx] > i+1:
                    canvas[5-i][idx] = i+1
                dir = 'L'
                idx-=1
    for i in range(6,10):
        if dir == 'L':
            if idx > 0:
                if canvas[i-5][idx] > i+1:
                    canvas[i-5][idx] = i+1
                idx-=1
            elif idx == 0:
                if canvas[i-5][idx] > i+1:
                    canvas[i-5][idx] = i+1
                dir = 'R'
                idx+=1
        elif dir == 'R':
            if idx < 5:
                if canvas[i-5][idx] > i+1:
                    canvas[i-5][idx] = i+1
                idx+=1
            elif idx == 5:
                if canvas[i-5][idx] > i+1:
                    canvas[i-5][idx] = i+1
                dir = 'L'
                idx-=1
for i in range(6):
    for j in range(6):
        if canvas[i][j] == 11:
            print('_',end='')
        else :
            print(canvas[i][j],end='')
    print()