T = int(input())

pw_dict = {'0001101' : '0', '0011001' : '1', '0010011': '2', '0111101' : '3',
           '0100011' : '4', '0110001' : '5', '0101111' : '6',
           '0111011' : '7', '0110111' : '8', '0001011' : '9'}
for tc in range(1,T+1):
    n, m = map(int, input().split())
    pw_code = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(m-1,-1,-1):
            if pw_code[i][j] == 1:
                pw_list = pw_code[i][j-55:j+1]
                break
    password = []
    for i in range(0,56,7):
        result = ''
        for j in range(7):
            result = result + str(pw_list[i+j])
        password.append(result)
    n_pw = []
    result = ''
    for p in password:
        if p in pw_dict:
            p = str(pw_dict[p])
        result = result + str(p)
    n_pw.append(result)
    valid_pw = 0
    pw = n_pw[0]
    A = int(pw[0]) + int(pw[2]) + int(pw[4]) + int(pw[6])
    B = int(pw[1]) + int(pw[3]) + int(pw[5]) + int(pw[7])
    if not (A*3 + B) % 10:
        valid_pw = A+B
    print(f'#{tc}',valid_pw)