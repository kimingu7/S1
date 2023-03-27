n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = []

def back():
    if len(seq) == m:
        print(*seq)
        return
    for i in lst:
        if i not in seq:
            seq.append(i)
            back()
            seq.pop()
back()

# N과 M 시리즈의 5번째 문제
# 이전 문제와 달리 이제는 주어진 list에서 수열을 조합함
# 이외에는 1번과 같음