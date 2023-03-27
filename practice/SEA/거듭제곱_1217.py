def square(n, m, k):
    while m > 1:
        k = k * n
        return square(n, m-1, k)
    return k

for i in range(10):
    t = int(input())
    n, m = map(int, input().split())
    k = n
    print(f'#{t} {square(n,m,k)}')


# 재귀호출을 이용해 푸는 문제
# 입력받은 n과 m과는 별개로 거듭제곱된 값을 저장해줄 k라는 별도의 값을 정의