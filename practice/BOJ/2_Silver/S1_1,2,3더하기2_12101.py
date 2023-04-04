def back(tmp, answer):
    global cnt
    if tmp > n:
        return
    if tmp == n:
        cnt+=1
        if cnt == k:
            print(answer[:-1])
            exit()
    for i in range(1,4):
        back(tmp+i, answer+str(i)+'+')

n, k = map(int, input().split())
cnt = 0
back(0, '')
print(-1)

# backtracking을 통해 푸는 문제
# 1부터 3까지 더해가며 tmp가 n보다 커질 때 return
# tmp가 n이 될 때 cnt를 1 증가시키고, cnt가 k라면 answer를 출력
# 백트래킹이 종료되었음에도 k번째 오는 식이 없을 경우 -1 출력