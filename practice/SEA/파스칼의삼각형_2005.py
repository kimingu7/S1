t = int(input())
for i in range(t):
    n = int(input())
    tri = [[0 for _ in range(n+1)] for _ in range(n+1)]
    tri[0][0] = 1
    for j in range(0,n):
        for k in range(0,n):
            tri[j+1][k+1] = tri[j][k] + tri[j][k+1]
    print(f'#{i+1}')
    for j in range(1,n+1):
        for k in range(1,n+1):
            if tri[j][k] != 0:
                print(tri[j][k],end=' ')
        print()

# 의도한대로 된건 아닌데 어찌저찌 출력은 함
# 2차원 배열로 생각했음
# [j+1][k+1]는 무조건 [j][k]와 [j][k+1]의 합인 것을 찾아내야함
# 0을 remove하려했으나 뜻대로 되지않았음
# 그래서 그냥 0이 아닐 때만 print하도록 했음