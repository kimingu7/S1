for i in range(10):
    t = int(input())
    canvas = [list(input()) for _ in range(100)]
    canvas_90 = [[0 for _ in range(100)] for _ in range(100)]
    for j in range(100):
        for k in range(100):
            canvas_90[j][k] = canvas[100-1-k][j]
    max_cnt = 0
    for j in range(100):
        for k in range(100):
            for l in range(100-k+1):
                if canvas[j][k:k+l] == list(reversed(canvas[j][k:k+l])):
                    cnt = len(canvas[j][k:k+l])
                    if max_cnt <= cnt:
                        max_cnt = cnt
                if canvas_90[j][k:k+l] == list(reversed(canvas_90[j][k:k+l])):
                    cnt = len(canvas_90[j][k:k+l])
                    if max_cnt <= cnt:
                        max_cnt = cnt
    print(f'#{t} {max_cnt}')

# 모든 경우의 수를 조사해야하는 Brute Force 유형의 문제
# 아주 단순하게 reversed를 사용해서 체크했음
# 근데 절반만큼 잘라서 ::-1 시킨 것과 앞부분이 같으면 회문인걸 알게됨