t = int(input())
for i in range(t):
    lst_n = list(input())
    cnt = 0
    c_cnt = 0
    for j in range(len(lst_n)):
        if lst_n[j] == '(':
            cnt+=1
        elif lst_n[j] == ')' :
            cnt-=1
        if cnt < 0 :
            print('NO')
            c_cnt+=1
            break
    if cnt == 0 and c_cnt == 0:
        print('YES')
    elif cnt != 0 and c_cnt == 0 :
        print('NO')