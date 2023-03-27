char = input()

if len(char) % 2 == 1:
    n = (len(char)//2)
    m = n+1
    ans = char[n:m]
    print(ans)
else :
    n = (len(char)//2) - 1
    m = n+2
    ans = char[n:m]
    print(ans)