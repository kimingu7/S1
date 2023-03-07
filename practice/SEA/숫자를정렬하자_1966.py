t = int(input())
for i in range(t):
    n = int(input())
    lst_n = list(map(int, input().split()))
    lst_n.sort()
    print(f'#{i+1} {" ".join(map(str,lst_n))}')

# 숫자를 정렬하면 됨