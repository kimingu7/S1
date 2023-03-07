t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    max_lst = lst[0]
    min_lst = lst[0]
    for j in range(n):
        if max_lst < lst[j]:
            max_lst = lst[j]
        if min_lst > lst[j]:
            min_lst = lst[j]
    print(f'#{i+1} {max_lst - min_lst}')