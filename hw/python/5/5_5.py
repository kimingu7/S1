words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

words_list = []
n_words_list = []
for key in words_dict:
    words_list.append(key)
for i in range(len(words_list)):
    if words_list[i][0] == 'r':
        n_words_list.append(f'ir{words_list[i]}')
    elif words_list[i][0] == 'l':
        n_words_list.append(f'il{words_list[i]}')
    elif words_list[i][0] == 'b' or words_list[i][0] == 'm' or words_list[i][0] == 'p':
        n_words_list.append(f'im{words_list[i]}')

print(n_words_list)