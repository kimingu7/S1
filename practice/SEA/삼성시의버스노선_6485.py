t = int(input())
for i in range(t):
    n = int(input())
    route = [[0 for _ in range(2)] for _ in range(n)]
    for j in range(n):
        route[j] = list(map(int, input().split()))
    p = int(input())
    station = [[0 for _ in range(1)] for _ in range(p)]
    result = [[0 for _ in range(1)] for _ in range(p)]
    for k in range(p):
        station[k] = int(input())
    for j in range(p):
        for k in range(n):
            if station[j] >= route[k][0] and station[j] <= route[k][1]:
                result[j][0]+=1
    lst_rst = []
    for j in range(p):
        lst_rst.append(result[j][0])
    print(f'#{i+1} {" ".join(map(str,lst_rst))}')