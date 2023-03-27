numbers = list(map(int,input().split()))
sum_nums = 0
for i in range(len(numbers)):
    sum_nums = sum_nums + (numbers[i] ** 2)
print(sum_nums % 10)