t = int(input())
for i in range(t):
    str = list(input())
    n = len(str)
    dia_str = [[0 for _ in range((n*4)+1)] for _ in range(5)]
    for j in range(5):
        for k in range((n*4)+1):
            dia_str[j][k] = '.'
    for j in range(2,(n*4),4):
        dia_str[0][j] = '#'
        dia_str[4][j] = '#'
    for j in range(1,(n*4)+1,2):
        dia_str[1][j] = '#'
        dia_str[3][j] = '#'
    for j in range(0,(n*4)+1,2):
        dia_str[2][j] = '#'
    for j in range(2,(n*4)+1,4):
        dia_str[2][j] = str[(j-2)//4]
    for j in dia_str:
        print(*j,sep='')

# 그냥 큰 의미 없는 노가다 문제