T = int(input())

for tc in range(1,T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    h = max(trees)
    one = 0
    two = 0
    for i in range(N):
        dif = h-trees[i]
        if dif%2:
            one+=1
            two+=dif//2
        else :
            two+=dif//2
    while two - one > 1:
        two-=1
        one+=2
    if two >= one:
        answer = two*2
    elif one == 0 and two == 0:
        answer = 0
    else :
        answer = one*2-1
    print(f'#{tc}',answer)
    
# GOD_ 성환