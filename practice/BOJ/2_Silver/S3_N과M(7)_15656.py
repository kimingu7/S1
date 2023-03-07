n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = []

def back(s):
    if len(seq) == m:
        print(*seq)
        return
    for i in range(n):
        seq.append(lst[i])
        back(i+1)
        seq.pop()
back(0)

# N과 M 시리즈의 7번째 문제
# 3번과 유사하게 중복 체크하는 부분을 빼주면 됨