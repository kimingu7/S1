t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input()))
    group = list(set(lst))
    rst = dict()
    for j in group:
        rst[j] = lst.count(j)
    rst = dict(sorted(rst.items(), key=lambda x: x[0]))
    rst = sorted(rst.items(), key=lambda x: x[1])
    print(f'#{i+1} {rst[-1][0]} {rst[-1][1]}')

# line 10 가장 큰 key를 기준으로 정렬, 한번 더 정렬해야해서 dict 사용
# line 11 가장 큰 value를 기준으로 정렬