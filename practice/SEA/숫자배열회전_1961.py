t = int(input())
for i in range(t):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    lst_270 = [[0 for _ in range(n)] for _ in range(n)]
    lst_180 = [[0 for _ in range(n)] for _ in range(n)]
    lst_90 = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        lst[j] = list(map(int, input().split()))
    for j in range(n):
        for k in range(n):
            lst_270[j][k] = lst[k][n-1-j] * 1
    for j in range(n):
        for k in range(n):
            lst_180[j][k] = lst[n-1-j][n-1-k] * 1
    for j in range(n):
        for k in range(n):
            lst_90[j][k] = lst[n-1-k][j] * 1
    print(f'#{i+1}')
    for k in range(n):
        for l in range(n):
            print(lst_90[k][l],end='')
        print(end=' ')
        for l in range(n):
            print(lst_180[k][l],end='')
        print(end=' ')
        for l in range(n):
            print(lst_270[k][l],end='')
        print('')

# 2차원 배열을 회전시키는 것보다 더 어려웠던 출력
# print(end=' ')로 각 배열 사이에 공백을 줘야했음