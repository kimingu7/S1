T = int(input())
x = [0 for _ in range(10**6+1)]
for i in range(1,10**6+1):
    x[i] = i**3
for tc in range(1, T+1):
    n = int(input())
    if n in x:
        ans = x.index(n)
    else :
        ans = -1
    print(f'#{tc}',ans)

# 10**18의 세제곱은은 10**6이므로 x의 범위를 0부터 10**6+1까지로 둠
# n이 x에 있다면 x.index(n)이 정답
# 아닐 경우 -1이 정답