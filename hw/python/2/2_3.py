str_lst = list(input().split())

if str_lst[0][-1].lower() == str_lst[1][0].lower() and str_lst[1][-1].lower() == str_lst[2][0].lower():
    print('pass')
else:
    print('fail')