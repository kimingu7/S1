import sys
n = int(sys.stdin.readline())
stack = []
ans = []
flag = 0
a = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while a <= num:
        stack.append(a)
        ans.append('+')
        a+=1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else :
        print('NO')
        flag = 1
        break
if flag == 0:
    for i in ans:
        print(i)