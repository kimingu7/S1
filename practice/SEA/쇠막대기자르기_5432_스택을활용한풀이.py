t = int(input())
for i in range(t):
    tc = input()
    stack = []
    cut = 0
    for j in range(len(tc)):
        if tc[j] == '(' and tc[j+1] == ')':
            cut+=len(stack)
        elif tc[j] == '(':
            stack.append(tc[j])
        elif tc[j] == ')' and tc[j-1] != '(':
            stack.pop()
            cut+=1
    print(f'#{i+1} {cut}')

# 스택을 활용해 풀었습니다
# 짧네요