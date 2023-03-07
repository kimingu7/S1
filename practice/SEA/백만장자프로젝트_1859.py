t = int(input())
for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    sum_price = 0
    max_price = price[-1]
    for j in range(n-2,-1,-1):
        if max_price <= price[j]:
            max_price = price[j]
        else :
            sum_price+=max_price - price[j]
    print(f'#{i+1} {sum_price}')

# 뒤에서부터 최대값이 바뀔 때마다 누적된 값에 최대값과 현재 값의 차를 더해줌