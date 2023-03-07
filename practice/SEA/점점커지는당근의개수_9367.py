t = int(input())
for i in range(t):
    n = int(input())
    lst_c = list(map(int,input().split()))
    cnt_lst = max_cnt = 0
    for j in range(n-1):
        if lst_c[j]+1 == lst_c[j+1]:
            cnt_lst+=1
        else :
            cnt_lst = 0
        if cnt_lst > max_cnt:
            max_cnt = cnt_lst
    print(f'#{i + 1} {max_cnt+1}')

# 연속해서 커지는 수 중 가장 많이 증가하는 구간의 길이를 구하면 됨