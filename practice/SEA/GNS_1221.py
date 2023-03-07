t = int(input())
for i in range(t):
    tc, n = input().split()
    str_ = list(input().split())
    priority_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
    str_.sort(key=lambda x:priority_dict[x])
    print(f'{tc}')
    for j in str_:
        print(j, end=' ')