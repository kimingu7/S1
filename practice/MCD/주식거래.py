T = int(input())

for tc in range(1, T+1):
    Ms, Ma = map(int, input().split())
    origin_Ms = Ms
    N, L = map(int, input().split())
    stocks = [list(map(int, input().split())) for _ in range(N)]
    benefits = [[0 for _ in range(N)] for _ in range(L-1)]
    benefit = tmp = answer = 0
    Ms -= Ma
    for i in range(N):
        for j in range(L-1):
            benefits[j][i] = (stocks[i][j], stocks[i][j] - stocks[i][j+1])
    for i in range(L-1):
        Ms = Ms + Ma + benefit
        benefits[i].sort(key=lambda x:x[1], reverse=True)
        if benefits[i][0][1] > 0:
            stock = Ms // benefits[i][0][0]
            tmp = stock * benefits[i][0][1]
            benefit += stock * benefits[i][0][1]
        if Ms - tmp > benefits[i][1][0]:
            stock2 = (Ms - tmp) // benefits[i][1][0]
            tmp2 = stock2 * benefits[i][1][1]
            benefit += stock2 * benefits[i][1][1]
    answer = Ms - origin_Ms - (Ma*L)
    print(f'#{tc}',answer)

# 솔직히 이건 틀린걸 아는데 고칠 엄두두두등장이 안남