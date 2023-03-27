char = [[0] * 15 for i in range(5)]
for i in range(5):
    n_char = list(input())
    n_char_len = len(n_char)
    for j in range(n_char_len):
        char[i][j] = n_char[j]
for i in range(15):
    for j in range(5):
        if char[j][i] == 0:
            continue
        else:
            print(char[j][i], end='')