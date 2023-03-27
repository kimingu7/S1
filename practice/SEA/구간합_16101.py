t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    lst = list(map(int,input().split()))
    sum_lst = []
    for j in range(n-m+1):
        sums = 0
        for k in range(m):
            sums = sums + lst[j+k]
        sum_lst.append(sums)
    print(f'#{i+1} {max(sum_lst)-min(sum_lst)}')

# 구간합을 구해서 최소 구간합과 최대 구간합의 차를 구함
# 구간합을 슬라이싱으로 구하면 더 짧을 것