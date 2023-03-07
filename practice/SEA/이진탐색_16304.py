t = int(input())
def binarySearch(p,key):
    start = 1
    end = p
    count = 0
    while start <= end:
        middle = int((start+end)/2)
        count += 1
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else :
            start = middle
for i in range(t):
    p, a, b = map(int, input().split())
    count_a = binarySearch(p,a)
    count_b = binarySearch(p,b)
    if count_a > count_b:
        rst = 'B'
    elif count_a < count_b:
        rst = 'A'
    elif count_a == count_b:
        rst = 0
    print(f'#{i+1} {rst}')