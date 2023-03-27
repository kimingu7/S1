T = int(input())
for tc in range(1,T+1):
    n = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    answer = 1000
    for i in range(n-2):
        for j in range(i+1,n-1):
            small = carrot[:i+1]
            medium = carrot[i+1:j+1]
            big = carrot[j+1:]
            if small[-1]!=medium[0] and medium[-1]!=big[0]:
                s = len(small)
                m = len(medium)
                b = len(big)
                max_box = max(s,m,b)
                min_box = min(s,m,b)
                if max_box <= n//2 and min_box > 0:
                    answer = min(answer, max_box-min_box)
    if answer == 1000:
        answer = -1
    print(f'#{tc}', answer)