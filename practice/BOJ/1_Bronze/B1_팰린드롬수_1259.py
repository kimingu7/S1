while True:
    num = int(input())
    if num == 0:
        break
    num_ = int(str(num)[::-1])
    if num == num_:
        print('yes')
    else :
        print('no')
    