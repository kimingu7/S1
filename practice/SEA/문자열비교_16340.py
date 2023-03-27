t = int(input())
for i in range(t):
    str1 = list(input())
    str2 = list(input())
    n = len(str1)
    m = len(str2)
    for j in range(m-n+1):
        n_str2 = str2[j:j+n]
        if n_str2 == str1:
            rst = 1
            break
        else :
            rst = 0
    print(f'#{i+1} {rst}')

# 슬라이싱을 활용해 같으면 1, 다르면 0 출력