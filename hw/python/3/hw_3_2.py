year = int(input())
if year % 400 == 0:
    print('leap year')
else:
    if year % 100 == 0:
        print('common year')
    else :
        if year % 4 == 0:
            print('leap year')
        else :
            print('common year')