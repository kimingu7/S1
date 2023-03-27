import sys
m = int(sys.stdin.readline())
S = set()
for i in range(m):
    tmp = sys.stdin.readline().strip().split()
    if len(tmp) == 1:
        if tmp[0] == 'all':
            S = set([i for i in range(1,21)])
        else :
            S = set()   
    else :
        order, x = tmp[0], tmp[1]
        x = int(x)
        if order == 'add':
            S.add(x)
        elif order == 'remove':
            S.discard(x)
        elif order == 'check':
            if x in S:
                print(1)
            else :
                print(0)
        elif order == 'toggle':
            if x in S:
                S.discard(x)
            else :
                S.add(x)

# 메모리 절약을 위해 set을 활용해서 풀어야함
# list와 달리 set에선 append 대신 add, remove 대신 discard를 사용함
# 그 이외엔 list와 같은 방법으로 풀면 됨