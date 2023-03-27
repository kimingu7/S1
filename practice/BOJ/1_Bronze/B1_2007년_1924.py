x, y = map(int,input().split())
date_from_new_year = 0
days_month = [31,28,31,30,31,30,31,31,30,31,30,31]
weekdays = ['SUN','MON','TUE','WED','THU','FRI','SAT']
for i in range(x-1):
    date_from_new_year = date_from_new_year + days_month[i]
date_from_new_year = date_from_new_year + y
for i in range(len(weekdays)):
    if date_from_new_year % 7 == i:
        print(weekdays[i])