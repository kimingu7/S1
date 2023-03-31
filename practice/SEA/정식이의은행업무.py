T = int(input())

for tc in range(1, T+1):
    binary = list(map(int,input()))
    trinary = list(map(int,input()))
    bi = tri = 0
    b = len(binary)
    t = len(trinary)
    for i in range(b):
        bi+=binary[i]*(2**(b-i-1))
    for i in range(t):
        tri+=trinary[i]*(3**(t-i-1))
    money = []
    for i in range(1, b):
        tmp = 0
        if binary[i] == 0:
            tmp = bi + (2**(b-i-1))
        else :
            tmp = bi - (2**(b-i-1))
        money.append(tmp)

    for i in range(t):
        tmp1 = 0
        tmp2 = 0
        if trinary[i] == 0 and i > 0:
            tmp1 = tri + (3**(t-i-1))
            tmp2 = tri + 2*(3**(t-i-1))
        elif trinary[i] == 1:
            if i == 0:
                tmp1 = tri + (3**(t-i-1))
            else:
                tmp1 = tri - (3**(t-i-1))
                tmp2 = tri + (3**(t-i-1))
        elif trinary[i] == 2:
            if i == 0:
                tmp1 = tri - (3**(t-i-1))
            else :
                tmp1 = tri - 2*(3**(t-i-1))
                tmp2 = tri - (3**(t-i-1))
        if tmp1 in money:
            answer = tmp1
        elif tmp2 in money:
            answer = tmp2
        money.append(tmp1)
        money.append(tmp2)
    print(f'#{tc}', answer)

# 삼진법을 잘못 생각해서 틀림