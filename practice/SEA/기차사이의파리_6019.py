t = int(input())
for i in range(t):
    d, a, b ,f = map(int,input().split())
    lgt = (d / (a+b)) * f
    print(f'#{i + 1} {lgt}')

# 간단한 방정식을 세우면 해결