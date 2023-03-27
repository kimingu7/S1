def babyjin(p):
    for j in range(10):
        if p[j] == 3:
            return True
    for k in range(8):
        if p[k] and p[k+1] and p[k+2]:
            return True
    return False

T = int(input())
for tc in range(1,T+1):
    card = list(map(int, input().split()))
    p1 = [0 for _ in range(10)]
    p2 = [0 for _ in range(10)]
    answer = 0
    for i in range(len(card)):
        if not i % 2:
            p1[card[i]] += 1
            if babyjin(p1):
                answer = 1
                break
        else :
            p2[card[i]] += 1
            if babyjin(p2):
                answer = 2
                break
    print(f'#{tc}', answer)