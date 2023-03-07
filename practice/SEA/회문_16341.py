t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    canvas = [list(input()) for _ in range(n)]
    for j in range(n):
        for k in range(n-m+1):
            str_1 = canvas[j][k:k+m]
            str_1_r = list(reversed(str_1))
            if str_1 == str_1_r:
                print(f"#{i+1} {''.join(str_1)}")
                break
    for j in range(n-m+1):
        for k in range(n):
            str_2 = []
            for l in range(m):
                str_2.append(canvas[j+l][k])
            str_2_r = list(reversed(str_2))
            if str_2 == str_2_r:
                print(f"#{i+1} {''.join(str_2)}")
                break