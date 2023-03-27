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
        if not visited[i] and printed_seq != lst[i]:
            visited[i] = 1
            seq.append(lst[i])
            printed_seq = lst[i]
            back(s+1)
            visited[i] = 0
            seq.pop()
back(0)

# N과 M 시리즈의 9번째 문제
# 주어진 수 중 중복된 숫자가 존재함
# 중복된 수열을 출력하지 않기 위해 visited 배열과 printed_seq라는 변수 활용