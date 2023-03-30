def merge_sort(arr):
    global cnt, merge_list
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merge_list = []
    l = h = 0
    while len(left) > l and len(right) > h:
        if left[l] <= right[h]:
            merge_list.append(left[l])
            l += 1
        else:
            merge_list.append(right[h])
            h += 1
    if len(left) > l:
        merge_list.extend(left[l:])
        cnt += 1
    else:
        merge_list.extend(right[h:])

    return merge_list

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    list_n = list(map(int, input().split()))
    cnt = 0
    merge_sort(list_n)
    answer = merge_list[n//2]
    print(f'#{tc}',answer, cnt)