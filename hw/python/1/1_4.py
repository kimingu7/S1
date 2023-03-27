sum_2 = sum_7 = sum_14 = 0
for i in range(1000):
    if i % 2 == 0:
        sum_2 = sum_2 + i
    if i % 7 == 0:
        sum_7 = sum_7 + i
    if i % 14 == 0:
        sum_14 = sum_14 + i
sum_27 = sum_2 + sum_7 - sum_14
print(sum_27)