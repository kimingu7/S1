for tc in range(10):
    n = int(input())
    str = input()
    stack = []
    rst=''
    for i in str:
        if i.isdigit():
            rst+=i
        else :
            if i == '(':
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':
                    rst+=stack.pop()
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    rst+=stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    rst+=stack.pop()
                stack.pop()
    while stack:
        rst+=stack.pop()

    stack = []
    for i in rst:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        else :
            stack.append(int(i))
    ans = stack.pop()
    print(f'#{tc+1} {ans}')