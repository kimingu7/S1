k = int(input())
lst = []
for i in range(k):
    a = int(input())
    if a == 0:
        del lst[-1]
    else:
        lst.append(a)
print(sum(lst))