for i in range(10):
    n, str = input().split()
    stack = []
    for j in range(0, len(str)):
        if len(stack) == 0:
            stack.append(str[j])
        elif stack[-1] != str[j]:
            stack.append(str[j])
        else:
            stack.pop()
    print(f'#{i+1}',''.join(stack))

# 반복문자지우기와 같은 문제