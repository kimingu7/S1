T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    if N % H == 0:
        N = (H * 100) + (N // H)
    else :
        N = ((N % H) * 100) + ((N // H) + 1)
    print(N)