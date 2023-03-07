a, b = map(int, input().split())
lst = []
for i in range(1,100):
    for j in range(1, i+1):
        lst.append(i)
print(sum(lst[a-1:b]))