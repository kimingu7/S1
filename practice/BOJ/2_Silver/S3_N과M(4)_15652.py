n, m = map(int, input().split())
seq = []

def back(s):
    if len(seq) == m:
        print(*seq)
        return
    for i in range(s,n+1):
        seq.append(i)
        back(i)
        seq.pop()
back(1)

# N과 M 시리즈의 네번째 문제
# 쉽게 말해서 2에서 3과 같이 if i not in seq를 빼주면 됨