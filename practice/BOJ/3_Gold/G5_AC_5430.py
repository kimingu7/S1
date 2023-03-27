import sys
t = int(sys.stdin.readline())
for i in range(t):
    cnt = 0
    rev = 0
    p = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    lst_n = list(sys.stdin.readline().strip('[').strip(']\n').split(','))
    if n == 0:
        lst_n = []
    for j in range(n):
        lst_n[j] = int(lst_n[j])
    for k in range(len(p)):
        if p[k] == 'R':
            rev+=1
        elif p[k] == 'D':
            if len(lst_n) > 0:
                if rev%2 == 1:
                    del lst_n[-1]
                else :
                    del lst_n[0]
            else :
                print('error')
                cnt=1
                break
    if cnt == 0:
        if rev%2 == 0:
            print(f'[{",".join((map(str,lst_n)))}]')
        else :
            lst_n.reverse()
            print(f'[{",".join((map(str,lst_n)))}]')