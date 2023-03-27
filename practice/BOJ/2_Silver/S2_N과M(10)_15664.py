n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0 for _ in range(n)]
seq = []

def back(s):
    if len(seq) == m:
        print(*seq)
        return
    printed_seq = 0
    for i in range(n):
        if not visited[i] and printed_seq != lst[i] and (len(seq) == 0 or seq[-1] <= lst[i]):
            visited[i] = 1
            seq.append(lst[i])
            printed_seq = lst[i]
            back(s+1)
            visited[i] = 0
            seq.pop()
back(0)

# N과 M 시리즈의 10번째 문제
# 이전 문제처럼 i의 범위를 s부터 n까지로 하려했으나 답이 맞지않음
# 따라서 len(seq) == 0이거나 seq[-1]이 lst[i]보다 작은 경우만 seq에 추가하는 조건을 추가