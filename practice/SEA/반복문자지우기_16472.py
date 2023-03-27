t = int(input())
for i in range(t):
    lst = list(input())
    stack = []
    for j in range(len(lst)):
        if len(stack) == 0:
            stack.append(lst[j])
        elif stack[-1] != lst[j]:
            stack.append(lst[j])
        else :
            stack.pop()
    print(f'#{i+1} {len(stack)}')

# 0번 인덱스를 stack에 추가한 뒤 1번부터 append시킴
# 직전에 넣은 문자와 중복되면 pop, 중복이 아니면 append시킴
# stack에 아무것도 없을 때 오류가 발생함
# stack에 아무것도 없을 때는 무조건 append하도록 설정
# stack의 길이를 출력