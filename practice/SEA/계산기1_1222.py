for i in range(10):
    n = int(input())
    cal = list(input())
    for j in range(1,n,2):
        cal[j], cal[j+1] = cal[j+1], cal[j]
    stack = []
    for j in cal:
        if j == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        else :
            stack.append(int(j))
    rst = stack.pop()
    print(f'#{i+1} {rst}')

# Forth보다 이게 더 쉬운데 왜 D4?