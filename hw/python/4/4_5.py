test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}
sleeping_list = []
cheating_list = []

for key, value in test_status.items():
     if value == 'cheating':
         cheating_list.append(key)
     if value == 'sleeping':
         sleeping_list.append(key)
cheating_list.sort()
print(cheating_list)

for i in cheating_list:
	del test_status[i]
for i in sleeping_list:
	test_status[i] = 'solving'
print(test_status)