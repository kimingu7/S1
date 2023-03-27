import sys
n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
stack = []
lazers = []
for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            lazers.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        lazers.append(0)
    stack.append([i, towers[i]])
print(*lazers)

# stack을 활용해서 풀어야함(안그러면 시간초과 뜸)
# stack은 이차원 배열로 저장됨([타워의 index][타워의 높이])
# stack에는 기준점보다 왼쪽에 있는 모든 타워의 index와 높이가 저장
# stack[-1][1](스택에 마지막 저장된 타워의 높이)가 towers[i]보다 클 때 lazers에(스택에 마지막 저장된 타워의 index + 1) 저장
# 아닐 경우, stack.pop()
# stack이 비었을 경우, lazers에 0 append