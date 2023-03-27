for i in range(10):
    n = int(input())
    box = list(map(int, input().split()))
    for j in range(n):
        a = max(box)
        b = min(box)
        ida = box.index(a)
        idb = box.index(b)
        box[ida]-=1
        box[idb]+=1
    print(f'#{i + 1} {max(box)-min(box)}')