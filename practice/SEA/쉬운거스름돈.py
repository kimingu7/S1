T = int(input())

for tc in range(1,T+1):
    n = int(input())
    money = [0 for _ in range(8)]
    for i in range(8):
        if not i%2:
            money[i] = n//(50000//(10**(i//2)))
            n -= money[i] * (50000//(10**(i//2)))
        else :
            money[i] = n//(10000//(10**(i//2)))
            n -= money[i] * (10000//(10**(i//2)))
    print(f'#{tc}')
    for m in money:
        print(m,end=' ')
    print()