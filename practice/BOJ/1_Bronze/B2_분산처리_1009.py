T = int(input())
for i in range(T):
    a, b = map(int,input().split())

    if a % 10 == 0 :
        print(10)
            
    elif b%4 == 0 :
        a = a**((b-1)%4+1)
        print(a%10)
            
    else :
        a = a**(b%4)
        print(a%10)