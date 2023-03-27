n, m = map(int, input().split())
chess = [[0 for _ in range(m)] for _ in range(n)]
result = []
for i in range(n):
    chess[i] = list(input())
for i in range(n-7):
    for j in range(m-7):
        case1 = 0
        case2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'B':
                        case1 += 1
                    if chess[a][b] != 'W':
                        case2 += 1
                else:
                    if chess[a][b] != 'W':
                        case1 += 1
                    if chess[a][b] != 'B':
                        case2 += 1
        result.append(case1)
        result.append(case2)
print(min(result))