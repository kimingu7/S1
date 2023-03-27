n, m = map(int, input().split())
seq = []

def back(s):
    if len(seq) == m:
        print(*seq)
        return
    for i in range(s, n+1):
        if i not in seq:
            seq.append(i)
            back(i+1)
            seq.pop()
back(1)

# N과 M 백트래킹 시리즈의 두번째 문제
# 1과 차이점은 증가하는 경우의 수만 출력한다는 것
# 증가하는 경우의 수만 출력하기 위해 line 8에서 범위를 s에서 n까지로 둠
# s를 받아오기 위해 함수에 매개변수 s를 둠
# 또한 매개변수를 증가시켜 다음 재귀함수를 불러옴