n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = []

def back(s):
    if len(seq) == m:
        print(*seq)
        return
    for i in range(s-1,n):
        seq.append(lst[i])
        back(i+1)
        seq.pop()
back(1)

# N과 M 시리즈의 8번째 문제
# 같은 수를 여러번 골라도 되는 문제
# 4번과 유사하게 풀면 됨
# 이 때 i의 범위는 s-1,n부터이고, 1부터 시작해야함