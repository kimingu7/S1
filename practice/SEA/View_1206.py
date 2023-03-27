for i in range(10):
    n = int(input())
    bd = list(map(int, input().split()))
    cnt = 0
    for j in range(2,n-2):
        view = [bd[j]-bd[j-2],bd[j]-bd[j-1],bd[j]-bd[j+1],bd[j]-bd[j+2]]
        if min(view) > 0:
            cnt = cnt + min(view)
    print(f'#{i + 1} {cnt}')