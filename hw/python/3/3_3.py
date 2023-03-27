infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
age = [0 for _ in range(len(infos))]
for i in range(len(infos)):
    age[i] = infos[i].get('age')
sum_age = 0
for i in range(len(age)):
    sum_age = sum_age + age[i]
print(sum_age)