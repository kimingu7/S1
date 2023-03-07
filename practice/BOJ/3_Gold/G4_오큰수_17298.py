import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
answer = [-1 for _ in range(n)]
stack = [0]
for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)

# 이중 for문으로 돌리게 될 경우 100% 시간초과 발생
# stack에 index를 담아줘야함
# A[stack[-1]] < A[i]일 때 (A에서 stack[-1]번째 수보다 오른쪽의 있는 수가 클 때)
# answer 배열의 stack.pop()의 값 stack[-1]번째 index = A[i]