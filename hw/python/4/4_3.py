# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

lst = [1, 1, 3, 3, 0, 1, 1]

for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
        lst[i] = ' '
while ' ' in lst:
    lst.remove(' ')
print(lst)