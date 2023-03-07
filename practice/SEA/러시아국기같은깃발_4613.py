def russia(W,B):
    row = 0
    count = 0
    while row < W:
        for j in range(m):
            if flags[row][j] != 'W':
                count+=1
        row+=1
    while row < W+B:
        for j in range(m):
            if flags[row][j] != 'B':
                count+=1
        row+=1
    while row < n:
        for j in range(m):
            if flags[row][j] != 'R':
                count+=1
        row+=1
    return count


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    flags = [list(input()) for _ in range(n)]
    result = 0
    min_count = n*m+1
    for i in range(1,n-1):
        for j in range(1,n-i):
            result = russia(i,j)
            if min_count > result:
                min_count = result
    print(f'#{tc}',min_count)

# 파란줄의 시작위치, 끝 위치에 따라 바뀌는 문자 수가 달라지는 브루트포스 문제
# i = 파란줄의 시작 위치, j = 파란줄 개수
# line 4 처음부터 파란 줄이 시작하기 전까지 W가 아닌 수 카운트
# line 9 파란 줄의 개수만큼 반복해서 B가 아닌 수 카운트
# lien 14 끝까지 R가 아닌 수 카운트