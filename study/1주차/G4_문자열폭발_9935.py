strs = input()
boom = input()
stack = []
boom_len = len(boom)
for i in range(len(strs)):
    stack.append(strs[i])
    if ''.join(stack[-boom_len:]) == boom:
        for _ in range(boom_len):
            stack.pop()
if stack:
    print(*stack,sep='')
else :
    print('FRULA')

# stack에 strs를 담다가 boom_len만큼 슬라이싱한 문자열이 boom과 같을 때
# stack에서 pop
# stack이 있을 경우 stack을 출력
# stack이 비었을 경우 FRULA 출력