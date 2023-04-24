N = int(input())
stack = []

cnt = 0
for i in range(N):
    buildings = int(input())
    if stack:
        if stack[-1] <= buildings:
            while stack and stack[-1] <= buildings:
                stack.pop()
            cnt += len(stack)
            stack.append(buildings)
        else:
            cnt += len(stack)
            stack.append(buildings)
    else :
        stack.append(buildings)
print(cnt)

# 탑 문제를 뒤집어서 한 문제인데, 개수만 세면 된다
# 특이한 부분은 입력이 한줄이 아니라 여러 줄로 주어지는데,
# 이 부분에 대한 배열을 따로 만들지 않고 동시에 처리한다는 것