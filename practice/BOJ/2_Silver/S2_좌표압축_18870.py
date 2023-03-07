n = int(input())
lst = list(map(int, input().split()))
n_lst = sorted(list(set(lst)))
d_lst = {n_lst[i] : i for i in range(len(n_lst))}
for i in lst:
    print(d_lst[i], end=' ')

# line 3 lst에서 중복을 제거한 후 정렬한 n_lst
# line 4 n_lst[i]를 key로, i를 value로 하는 딕셔너리 d_lst
# line 5-6 lst[i]의 key와 일치하는 d_lst의 value 출력