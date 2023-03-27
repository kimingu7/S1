from collections import Counter
entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

count_entry = dict(Counter(entry_record))
count_exit = dict(Counter(exit_record))
n_count_entry = sorted(count_entry.items(), key=lambda x:x[1], reverse=True)
print('입장 기록 많은 Top3')
for i in range(3):
    print(f'{n_count_entry[i][0]} {n_count_entry[i][1]}회')

count_entry = sorted(count_entry.items())
count_exit = sorted(count_exit.items())
print('\n출입 기록이 수상한 사람')
for i in range(len(count_entry)):
    if count_entry[i][1] != count_exit[i][1]:
        if count_entry[i][1] < count_exit[i][1]:
            print(f'{count_entry[i][0]}은 퇴장 기록이 {count_exit[i][1] - count_entry[i][1]}회 더 많아 수상합니다')
        else :
            print(f'{count_entry[i][0]}은 입장 기록이 {count_entry[i][1] - count_exit[i][1]}회 더 많아 수상합니다')