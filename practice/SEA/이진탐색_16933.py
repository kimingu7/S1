def binarySearch(key, list_1):
    start = 0
    end = n-1
    before = ''
    while start <= end:
        middle = int((start+end)/2)
        if list_1[middle] == key:
            return True
        elif list_1[middle] > key:
            if before == 'left':
                return False
            end = middle - 1
            before = 'left'
        elif list_1[middle] < key:
            if before == 'right':
                return False
            start = middle + 1
            before = 'right'
    return False
T = int(input())

for tc in range(1,T+1):
    n, m = map(int, input().split())
    list_1 = list(map(int, input().split()))
    list_2 = list(map(int, input().split()))
    list_1.sort()
    answer = 0
    for key in list_2:
        if binarySearch(key, list_1):
            answer+=1
    print(f'#{tc}', answer)