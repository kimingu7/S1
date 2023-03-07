t = int(input())
def make_outer(lst, st, length, num):
    last = st+length-1
    for c in range(st, last+1):
        lst[st][c] = num
        num += 1
    for r in range(st+1, last+1):
        lst[r][last] = num
        num += 1
    for c in range(last-1, st-1,-1):
        lst[last][c] = num
        num += 1
    for r in range(last-1, st, -1):
        lst[r][st] = num
        num += 1
    return num
for i in range(t):
    n = int(input())
    lst = [[0 for j in range(n)] for k in range(n)]
    num, st = 1, 0
    while n > 0:
        num = make_outer(lst, st, n, num)
        n -= 2
        st += 1
    print(f'#{i+1}')
    for i in lst:
        print(*i)
