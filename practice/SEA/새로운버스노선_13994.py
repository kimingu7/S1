t = int(input())
for i in range(t):
    n = int(input())
    lst_st = []
    for j in range(n):
        tp, a, b = map(int,input().split())
        if tp == 1:
            for k in range(a,b+1):
                lst_st.append(k)
        elif tp == 2:
            lst_st.append(a)
            if a%2 == 1:
                for k in range(a+1,b):
                    if k%2 == 1:
                        lst_st.append(k)
            else:
                for k in range(a+1,b):
                    if k%2 == 0:
                        lst_st.append(k)
            lst_st.append(b)
        elif tp == 3:
            lst_st.append(a)
            if a%2 == 1:
                for k in range(a+1,b):
                    if k%3 == 0 and k%10 != 0:
                        lst_st.append(k)
            else :
                for k in range(a+1,b):
                    if k%4 == 0:
                        lst_st.append(k)
            lst_st.append(b)
    count={}
    for x in lst_st:
        if x in count:
            count[x]+=1
        else :
            count[x] = 1
    print(f'#{i+1} {max(count.values())}')