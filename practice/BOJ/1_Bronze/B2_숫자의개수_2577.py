a = int(input())
b = int(input())
c = int(input())
mlt_abc = a * b * c
mlt_abc = list(map(int, str(mlt_abc)))

for i in range(10):
    count = 0
    for j in range(len(mlt_abc)):
        if i == mlt_abc[j]:
            count+=1
    print(count)