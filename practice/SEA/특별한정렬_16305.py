t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = [0 for _ in range(10)]
    for j in range(n-1):
        maxIdx = j
        for k in range(j+1, n):
            if lst[maxIdx] < lst[k]:
                maxIdx = k
        lst[j], lst[maxIdx] = lst[maxIdx], lst[j]
    for j in range(5):
        ans[j*2] = lst[j]
    for j in range(n-1):
        minIdx = j
        for k in range(j+1, n):
            if lst[minIdx] > lst[k]:
                minIdx = k
        lst[j], lst[minIdx] = lst[minIdx], lst[j]
    for j in range(5):
        ans[j*2+1] = lst[j]
    print(f'#{i+1} {" ".join(map(str,ans))}')

# max와 min 두 번 정렬
# line 12-13에서 짝수 index에 max로 정렬한 값 순서대로 5개까지 저장
# line 20-21에서 홀수 index에 min로 정렬한 값 순서대로 5개까지 저장