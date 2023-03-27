t = int(input())
for i in range(t):
    lst = list(input().split())
    stack = []
    for j in lst:
        try :
            if j == '+' or j == '-' or j == '/' or j == '*':
                b = stack.pop()
                a = stack.pop()
                if j == '+':
                    stack.append(a+b)
                elif j == '-':
                    stack.append(a-b)
                elif j == '/':
                    stack.append(int(a/b))
                elif j == '*':
                    stack.append(a*b)
            elif j == '.':
                rst = stack.pop()
                if not stack:
                    print(f'#{i+1} {rst}')
                else :
                    print(f'#{i+1} error')
                break
            else :
                stack.append(int(j))
        except IndexError:
            print(f'#{i+1} error')
            break

# 후위 표기법을 응용해서 푸는 문제
# stack을 활용해 푸는 문제로 stack에서 두개의 수를 꺼내 연산한 뒤 다시 stack에 넣음
# try except 구문을 이용해 스택에 남은 수가 하나인데 연산자가 있을 경우 error 출력
# .이 입력되어 게산이 끝났음에도 스택에 남은 수가 있을 때도 error 출력