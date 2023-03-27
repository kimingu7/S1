t = int(input())
for i in range(t):
    n = int(input())
    lst_n = list(map(int, input()))
    cnt_lst = max_cnt = 0
    for j in range(n):
        if lst_n[j] == 1:
            cnt_lst+=1
        if lst_n[j] == 0:
            cnt_lst = 0
        if cnt_lst > max_cnt:
            max_cnt = cnt_lst
    print(f'#{i + 1} {max_cnt}')

# 연속한 1의 개수를 cnt_lst에 카운트 한 뒤에
# max_cnt보다 크면 max_cnt = cnt_lst