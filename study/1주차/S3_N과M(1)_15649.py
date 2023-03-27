n, m = map(int, input().split())
seq = []

def back():
    if len(seq) == m:
        print(*seq)
        return
    for i in range(1, n+1):
        if i not in seq:
            seq.append(i)
            back()
            seq.pop()

back()

# 백트래킹을 활용해서 푸는 문제, DFS와 달리 모든 경우의 수를 탐색하지 않음
# 본 문제는 재귀를 이용해 구현
# n = 3, m = 2일 때
# 1 2, 1 3, 2 1, 2 3, 3 1, 3 2의 경우로 나뉘는데
# line 9에서 1부터 n까지 첫번째 칸을 지정하고,
# line 10-13에서 seq 안에 중복되지 않는 수를 차례대로 append시킴

# * 백트래킹이 아닌 내장 함수를 이용한 순열로 풀이했을 때
# from itertools import permutations
# n, m = map(int, input().split())
# p = permutations(range(1, n+1), m)
# for i in p:
#     print(" ".join(map(str, i)))
