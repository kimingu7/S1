t = int(input())
for i in range(t):
    lst = list(input())
    stack = []
    rst = True
    for j in range(len(lst)):
        if lst[j] == '(' or lst[j] == '{':
            stack.append(lst[j])
        elif lst[j] == ')':
            if not stack or stack[-1] == '{':
                rst = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif lst[j] == '}':
            if not stack or stack[-1] == '(':
                rst = False
                break
            elif stack[-1] == '{':
                stack.pop()
    if rst and not stack:
        print(f'#{i+1} 1')
    else :
        print(f'#{i+1} 0')

# line 7 ( 또는 {를 입력 받았을 때 스택에 append
# line 9-12 )를 입력받았을 때 스택이 비어있거나, 마지막으로 스택에 저장된 문자가 {일 경우 False
# line 13-14 )를 입력받았을 때 마지막으로 스택에 저장된 문자가 (일 경우 스택에서 pop
# line 15-18 }를 입력받았을 때 스택이 비어있거나, 마지막으로 스택에 저장된 문자가 (일 경우 False
# line 19-20 }를 입력받았을 때 마지막으로 스택에 저장된 문자가 {일 경우 스택에서 pop
# line 21-22 for문을 종료했을 때 rst가 True이면서 stack이 비어있을 때 1 출력
# lien 23-24 나머지 경우 0 출력