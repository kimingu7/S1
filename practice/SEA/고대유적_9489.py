def max_len():
    max_site = 0
    for a in range(n):
        cnt = 0
        for b in range(m):
            if site[a][b] == 1:
                cnt+=1
            elif site[a][b] == 0:
                if max_site < cnt:
                    max_site = cnt
                    cnt = 0
                else :
                    cnt = 0
        if max_site < cnt:
            max_site = cnt
    for b in range(m):
        cnt = 0
        for a in range(n):
            if site[a][b] == 1:
                cnt+=1
            elif site[a][b] == 0:
                if max_site < cnt:
                    max_site = cnt
                    cnt = 0
                else :
                    cnt = 0
        if max_site < cnt:
            max_site = cnt
    return max_site

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    site = [list(input().split()) for _ in range(n)]
    for j in range(n):
        for k in range(m):
            site[j][k] = int(site[j][k])
    print(f'#{i+1} {max_len()}')

# 단순하게 행 순회 열 순회 두번 돌려서 연속된 1 카운트함
# 그리고 카운트 값이 최대값일 때 max_site 값을 바꿔줌