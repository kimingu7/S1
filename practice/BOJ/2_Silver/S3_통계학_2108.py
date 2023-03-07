from collections import Counter
def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes
n = int(input())
lst = [0 for _ in range(n)]
for i in range(n):
    lst[i] = int(input())
lst.sort()
print(round(sum(lst)/n))
print(lst[(len(lst)//2)])
if len(modefinder(lst)) > 1:
    print(modefinder(lst)[1])
else :
    print(modefinder(lst)[0])
print(max(lst)-min(lst))

