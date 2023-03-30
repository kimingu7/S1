def is_promising(q):
    for i in range(q):
        if row[q] == row[i] or abs(row[q] - row[i]) == abs(q-i):
            return False
    return True

def n_queens(q):
    global answer
    if q == n:
        answer+=1
        return
    else :
        for i in range(n):
            row[q] = i
            if is_promising(q):
                n_queens(q+1)
T = int(input())
for tc in range(1,T+1):
    n = int(input())

    answer = 0
    row = [0 for _ in range(n)]

    n_queens(0)
    print(f'#{tc}',answer)

# 끝까지 도달할 수 있을 때 answer에 1을 더함
# 유효성 검사를 통과하지 못한다면 분기 종료