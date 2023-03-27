num_list = [4, 4, 7, 8, 10, 4]
x = []
new_list = []

for i in num_list:
    if i not in x:
        x.append(i)
    else:
        if i not in new_list:
            new_list.append(i)

for i in range(len(num_list)):
    for j in range(len(new_list)):
        if num_list[i] == new_list[j]:
            num_list[i] = 0
print(sum(num_list))