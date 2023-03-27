n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = []

def back(s):
    if len(seq) == m:
        print(*seq)
        return
    for i in range(s,n):
        if lst[i] not in seq:
            seq.append(lst[i])
            back(i+1)
            seq.pop()
back(0)

# N과 M 시리즈의 6번째 문제
# 2번과 유사하게 시작점 s를 바꿔줘야함