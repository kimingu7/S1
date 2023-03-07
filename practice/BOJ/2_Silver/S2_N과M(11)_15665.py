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
        if printed_seq != lst[i]:
            seq.append(lst[i])
            printed_seq = lst[i]
            back(s+1)
            seq.pop()
back(0)

# N과 M 시리즈의 11번째 문제
# 중복된 수열을 출력하지 않기 위한 printed_seq는 유지
# visited 배열은 제거