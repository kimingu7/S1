T = int(input())

for tc in range(1,T+1):
    n = float(input())
    k = 1
    num = 0
    result = ''
    while k < 13:
        num = num+(2**(-k))
        if num < n:
            result = result + str(1)
        elif num > n:
            num-=(2**(-k))
            result = result + str(0)
        else :
            result = result + str(1)
            break
        k+=1
    if k == 13 and num != n:
        answer = 'overflow'
    else :
        answer = result
    print(f'#{tc}', answer)