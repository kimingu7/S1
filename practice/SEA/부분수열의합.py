def back(i):
    global answer, tmp
    if tmp > k:
        return
    if tmp == k:
        answer+=1
        return
    if i == n:
        if tmp == k:
            answer+=1
        return
    for j in range(i+1,n):
        if not visited[j]:
            tmp += list_n[j]
            visited[j] = 1
            back(j)
            visited[j] = 0
            tmp -= list_n[j]

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    list_n = list(map(int, input().split()))
    visited = [0 for _ in range(n)]
    answer = 0
    for i in range(n):
        tmp = list_n[i]
        back(i)
    print(f'#{tc}', answer)