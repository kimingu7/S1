import calendar

year = int(input())
month = int(input())
date = int(input())
day = calendar.weekday(year, month, date)
if day == 0:
    day = '월요일'
elif day == 1:
    day = '화요일'
elif day == 2:
    day = '수요일'
elif day == 3:
    day = '목요일'
elif day == 4:
    day = '금요일'
elif day == 5:
    day = '토요일'
elif day == 6:
    day = '일요일'

dict_date = {'년' : year, '월' : month, '일' : date, '요일' : day}

if year % 400 == 0:
    print('윤년입니다. 연도를 다시 입력해주세요.')
else:
    if year % 100 == 0:
        print(calendar.calendar(year))
        if day == '월요일':
            print('경고 월요일입니다')
        print(dict_date)
    else :
        if year % 4 == 0:
            print('윤년입니다. 연도를 다시 입력해주세요.')
        else :
            print(calendar.calendar(year))
            if day == '월요일':
                print('경고 월요일입니다')
            print(dict_date)