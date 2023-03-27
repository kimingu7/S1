password = list('password')
pw_list = [[0 for _ in range(len(password))] for _ in range(3)]
for i in range(3):
    pw_list[i] = list(input())
    if pw_list[i] == password:
        print("로그인 성공")
        break
    elif i == 2:
        print('3회 이상 틀렸습니다')