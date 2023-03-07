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

# 계산기2와 3의 풀이가 같아 한번에 작성
# 빈 문자열 rst에 입력받은 식을 후위표기법으로 저장
# 그 후 forth와 같은 방식으로 계산하면 됨