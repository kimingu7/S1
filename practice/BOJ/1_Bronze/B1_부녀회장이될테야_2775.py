t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    apart = [[1 for _ in range(n)] for _ in range(k+1)]
    for h in range(1,n):
        apart[0][h] = h+1
    for f in range(1,k+1):
        for h in range(1,n):
            apart[f][h] = apart[f-1][h] + apart[f][h-1]
    print(apart[k][n-1])