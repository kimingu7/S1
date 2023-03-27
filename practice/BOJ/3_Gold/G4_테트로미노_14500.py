n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
di1_1 = [0, 1, 2, 3]
dj1_1 = [0, 0, 0, 0]
di1_2 = [0, 0, 0, 0]
dj1_2 = [0, 1, 2, 3]

di2 = [0, 0, 1, 1]
dj2 = [0, 1, 0, 1]

di3_1 = [0, 1, 2, 2]
dj3_1 = [0, 0, 0, 1]
di3_2 = [0, 1, 2, 2]
dj3_2 = [0, 0, 0, -1]
di3_3 = [0, 0, 1, 2]
dj3_3 = [0, 1, 0, 0]
di3_4 = [0, 0, 1, 2]
dj3_4 = [0, 1, 1, 1]
di3_5 = [0, 1, 1, 1]
dj3_5 = [0, 0, 1, 2]
di3_6 = [0, 0, 0, 1]
dj3_6 = [0, 1, 2, 2]
di3_7 = [0, 0, 0, 1]
dj3_7 = [0, 1, 2, 0]
di3_8 = [0, 0, 0, -1]
dj3_8 = [0, 1, 2, 2]

di4_1 = [0, 1, 1, 2]
dj4_1 = [0, 0, 1, 1]
di4_2 = [0, 1, 1, 2]
dj4_2 = [0, 0, -1, -1]
di4_3 = [0, 0, -1, -1]
dj4_3 = [0, 1, 1, 2]
di4_4 = [0, 0, 1, 1]
dj4_4 = [0, 1, 1, 2]

di5_1 = [0, 0, 0, 1]
dj5_1 = [0, 1, 2, 1]
di5_2 = [0, 1, 1, 2]
dj5_2 = [0, 0, 1, 0]
di5_3 = [0, 0, -1, 0]
dj5_3 = [0, 1, 1, 2]
di5_4 = [0, -1, 0, 1]
dj5_4 = [0, 1, 1, 1]

max_sum = 0

def valid_ij(i,j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    return 1

for i in range(n):
    for j in range(m):
        sum1_1 = sum1_2 = sum2 = sum2 = 0
        sum3_1 = sum3_2 = sum3_3 = sum3_4 = 0
        sum3_5 = sum3_6 = sum3_7 = sum3_8 = 0
        sum4_1 = sum4_2 = sum4_3 = sum4_4 = 0
        sum5_1 = sum5_2 = sum5_3 = sum5_4 = 0
        for k in range(4):
            ni1_1, nj1_1 = i + di1_1[k], j + dj1_1[k]
            if valid_ij(ni1_1, nj1_1):
                sum1_1+=board[ni1_1][nj1_1]
            ni1_2, nj1_2 = i + di1_2[k], j + dj1_2[k]
            if valid_ij(ni1_2, nj1_2):
                sum1_2 += board[ni1_2][nj1_2]
            ni2, nj2 = i + di2[k], j + dj2[k]
            if valid_ij(ni2, nj2):
                sum2 += board[ni2][nj2]
            ni3_1, nj3_1 = i + di3_1[k], j + dj3_1[k]
            if valid_ij(ni3_1, nj3_1):
                sum3_1 += board[ni3_1][nj3_1]
            ni3_2, nj3_2 = i + di3_2[k], j + dj3_2[k]
            if valid_ij(ni3_2, nj3_2):
                sum3_2 += board[ni3_2][nj3_2]
            ni3_3, nj3_3 = i + di3_3[k], j + dj3_3[k]
            if valid_ij(ni3_3, nj3_3):
                sum3_3 += board[ni3_3][nj3_3]
            ni3_4, nj3_4 = i + di3_4[k], j + dj3_4[k]
            if valid_ij(ni3_4, nj3_4):
                sum3_4 += board[ni3_4][nj3_4]
            ni3_5, nj3_5 = i + di3_5[k], j + dj3_5[k]
            if valid_ij(ni3_5, nj3_5):
                sum3_5 += board[ni3_5][nj3_5]
            ni3_6, nj3_6 = i + di3_6[k], j + dj3_6[k]
            if valid_ij(ni3_6, nj3_6):
                sum3_6 += board[ni3_6][nj3_6]
            ni3_7, nj3_7 = i + di3_7[k], j + dj3_7[k]
            if valid_ij(ni3_7, nj3_7):
                sum3_7 += board[ni3_7][nj3_7]
            ni3_8, nj3_8 = i + di3_8[k], j + dj3_8[k]
            if valid_ij(ni3_8, nj3_8):
                sum3_8 += board[ni3_8][nj3_8]
            ni4_1, nj4_1 = i + di4_1[k], j + dj4_1[k]
            if valid_ij(ni4_1, nj4_1):
                sum4_1 += board[ni4_1][nj4_1]
            ni4_2, nj4_2 = i + di4_2[k], j + dj4_2[k]
            if valid_ij(ni4_2, nj4_2):
                sum4_2 += board[ni4_2][nj4_2]
            ni4_3, nj4_3 = i + di4_3[k], j + dj4_3[k]
            if valid_ij(ni4_3, nj4_3):
                sum4_3 += board[ni4_3][nj4_3]
            ni4_4, nj4_4 = i + di4_4[k], j + dj4_4[k]
            if valid_ij(ni4_4, nj4_4):
                sum4_4 += board[ni4_4][nj4_4]
            ni5_1, nj5_1 = i + di5_1[k], j + dj5_1[k]
            if valid_ij(ni5_1, nj5_1):
                sum5_1 += board[ni5_1][nj5_1]
            ni5_2, nj5_2 = i + di5_2[k], j + dj5_2[k]
            if valid_ij(ni5_2, nj5_2):
                sum5_2 += board[ni5_2][nj5_2]
            ni5_3, nj5_3 = i + di5_3[k], j + dj5_3[k]
            if valid_ij(ni5_3, nj5_3):
                sum5_3 += board[ni5_3][nj5_3]
            ni5_4, nj5_4 = i + di5_4[k], j + dj5_4[k]
            if valid_ij(ni5_4, nj5_4):
                sum5_4 += board[ni5_4][nj5_4]
        max_sum = max(sum1_1, sum1_2, sum2, sum3_1, sum3_2,
                      sum3_3, sum3_4, sum3_5, sum3_6, sum3_7, sum3_8,
                      sum4_1, sum4_2, sum4_3, sum4_4, sum5_1, sum5_2,
                      sum5_3, sum5_4, max_sum)
print(max_sum)