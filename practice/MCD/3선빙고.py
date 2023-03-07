bingo = [list(map(int, input().split())) for _ in range(5)]
mc = []
cnt = 0
for _ in range(5):
    mc += list(map(int, input().split()))

def check_bingo():
    count_bingo = 0

    for x in bingo:
        if x.count(0) == 5:
            count_bingo +=1

    for i in range(5):
        y = 0
        for j in range(5):
            if bingo[j][i] == 0:
                y+=1
        if y == 5:
            count_bingo+=1

    dig1 = 0
    for i in range(5):
        if bingo[i][j] == 0:
            dig1+=1
    if dig1 == 5:
        count_bingo+=1

    dig2 = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            dig2+=1
    if dig2 == 5:
        count_bingo+=1

    return count_bingo

for i in range(25):
    for x in range(5):
        for y in range(5):
            if mc[i] == bingo[x][y]:
                bingo[x][y] = 0
    if check_bingo() >= 3:
        print(mc[i])
        exit()