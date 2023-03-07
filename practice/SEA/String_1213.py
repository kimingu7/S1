def boyermoore(b,a):
    m = len(b)
    n = len(a)
    i = 0
    cnt = 0
    while i <= n-m:
        j = m-1
        while j >= 0:
            if b[j] != a[i+j]:
                move = find(b,a[i+m-1])
                break
            j = j-1
        if j == -1:
            cnt+=1
            i+=m
        else :
            i+=move
    return cnt

def find(b, char):
    for i in range(len(b)-2,-1,-1):
        if b[i] == char:
            return len(b)-i-1
    return len(b)

for i in range(10):
    t = int(input())
    b = input()
    a = input()
    cnt = boyermoore(b,a)
    print(f'#{t} {cnt}')

# 가장 빠른 문자열 타이핑을 붙여넣기 했더니 맞음