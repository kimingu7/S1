N, M, K = map(int, input().split())

canvas = [[[] for _ in range(N)] for _ in range(N)]
fireball = []
for i in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireball.append([r,c,m,s,d])
cnt = 0
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    while fireball:
        r1, c1, m1, s1, d1 = fireball.pop(0)
        nr = (r1 + s1 * dr[d1]) % N
        nc = (c1 + s1 * dc[d1]) % N
        canvas[nr][nc].append([m1, s1, d1])
    for r in range(N):
        for c in range(N):
            if len(canvas[r][c]) > 1:
                sum_m = sum_s = odd = even = 0
                cnt = len(canvas[r][c])
                while canvas[r][c]:
                    m2, s2, d2 = canvas[r][c].pop(0)
                    sum_m+=m2
                    sum_s+=s2
                    if d2 % 2:
                        odd+=1
                    else :
                        even+=1
                if odd == cnt or even == cnt:
                    nd = [0,2,4,6]
                else :
                    nd = [1,3,5,7]
                if sum_m//5:
                    for d in nd:
                        fireball.append([r,c,sum_m//5, sum_s//cnt, d])
            if len(canvas[r][c]) == 1:
                fireball.append([r,c] + canvas[r][c].pop())

print(sum([fb[2] for fb in fireball]))

# fireball에 r,c,m,s,d 정보 저장
# fireball마다 이동시킨 정보를 canvas 배열에 배열로 저장
# canvas[r][c]에 저장된 배열의 개수 = 중첩된 파이어볼의 수
# 중첩된 파이어볼의 방향을 계산해 4개로 분할
# k번 이동시킨 후 남은 fireball의 질량의 합 계산