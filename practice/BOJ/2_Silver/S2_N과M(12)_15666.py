n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = []

def back(s):
    if len(seq) == m:
        print(*seq)
        return
    printed_seq = 0
    for i in range(n):
        if printed_seq != lst[i] and (len(seq) == 0 or seq[-1] <= lst[i]):
            seq.append(lst[i])
            printed_seq = lst[i]
            back(s+1)
            seq.pop()
back(0)

# N과 M 시리즈의 마지막 문제
# 사전 순으로 증가하는 수열만 출력하기 위해 10번과 같은 조건 추가