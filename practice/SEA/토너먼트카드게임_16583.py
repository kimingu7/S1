def rps(a,b):
    if lst[a] == lst[b]:
        return a
    elif lst[a] + lst[b] == 4:
        if lst[a] == 1:
            return a
        else :
            return b
    else :
        if lst[a] > lst[b]:
            return a
        else :
            return b

def game(i, j):
    if i == j:
        return i
    p1 = game(i,(i+j)//2)
    p2 = game((i+j)//2+1,j)
    return rps(p1,p2)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    champion = game(0,n-1)
    print(f'#{tc} {champion+1}')

# 분할정복을 활용하여 토너먼트의 조를 나누는 게임
# 가위바위보는 간단한 함수이기에 큰 의미를 두지 않음
# 문제에서 제시한 i, (i+j)//2 와 (i+j)//2+1, j 두 그룹으로 팀의 크기가 1 또는 2가 될 때까지 쪼갠다는 것을 인지
# game에서 i == j와 rps에서 lst[a] == lst[b]는 다름 (전자의 경우 팀의 크기가 1, 후자의 경우 경기를 비김)