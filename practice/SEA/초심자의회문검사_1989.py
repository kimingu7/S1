t = int(input())
 
for i in range(t):
    str = list(input())
    str_ = list(reversed(str))
    if str == str_:
        print(f'#{i+1} {1}')
    else :
        print(f'#{i+1} {0}')

# reversed 쓰면 쉬운 문제
# 근데 길이가 길어진다면 분명 시간초과 뜸