participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

count={}
for x in participants:
    if x in count:
        count[x]+=1
    else :
        count[x] = 1
print(*[k for k, v in count.items() if v == 1])