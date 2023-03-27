n, m = map(int, input().split())
seq = []

def back():
    if len(seq) == m:
        print(*seq)
        return
    for i in range(1, n+1):
        seq.append(i)
        back()
        seq.pop()
back()

# N과 M 시리즈의 세번째 문제
# 1과 유사하나 1 1, 2 2와 같이 같은 수를 사용해도 가능함
# 그럼 1에서 중복 체크를 위해 사용했던 if i not in seq를 빼면 됨