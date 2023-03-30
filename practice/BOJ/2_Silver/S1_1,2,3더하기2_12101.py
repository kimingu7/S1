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