cnt = 1
while True:
    words_1 = input()
    words_2 = input()
    if words_1 == 'END' and words_2 == 'END':
        break
    words_1 = list(words_1)
    words_2 = list(words_2)
    words_1.sort()
    words_2.sort()
    if words_1 == words_2:
        print(f'Case {cnt}: same')
    else :
        print(f'Case {cnt}: different')
    cnt+=1